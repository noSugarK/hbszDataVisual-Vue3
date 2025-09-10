from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import USER
from .serializers import UserProfileSerializer, UserDetailSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    """
    用户个人信息视图
    允许用户查看和更新自己的信息
    """
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # 返回当前登录用户
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_detail_view(request, user_id):
    """
    获取指定用户详情（用于管理员查看）
    """
    # 检查用户是否存在
    user = get_object_or_404(USER, id=user_id)
    
    # 权限检查：
    # 1. 用户本人可以查看
    # 2. 超级管理员可以查看
    # 3. 管理员可以查看
    if (request.user == user or 
        request.user.is_superuser or 
        request.user.is_staff):
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)
    else:
        return Response(
            {'detail': '您没有权限查看此用户信息'}, 
            status=status.HTTP_403_FORBIDDEN
        )