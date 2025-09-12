from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import USER
from .serializers import UserProfileSerializer, UserCreateUpdateSerializer
from .permissions import IsSuperuserOrStaff, IsSuperuser, IsOwnerOrAdmin


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


class UserListView(generics.ListCreateAPIView):
    """用户列表与创建视图"""
    queryset = USER.objects.all()
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsSuperuserOrStaff]

    def perform_create(self, serializer):
        # 记录创建者
        serializer.save(created_by=self.request.user)


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """用户详情、更新、删除视图"""
    queryset = USER.objects.all()
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def update(self, request, *args, **kwargs):
        # 普通用户更新时不能修改权限字段
        if not (request.user.is_superuser or request.user.is_staff):
            # 移除权限相关字段，防止普通用户修改
            data = request.data.copy()
            data.pop('is_superuser', None)
            data.pop('is_staff', None)
            request._full_data = data
        return super().update(request, *args, **kwargs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_username_exists(request):
    """
    检查用户名是否已存在
    """
    username = request.GET.get('username', None)
    if not username:
        return Response({'error': '用户名不能为空'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 检查用户名是否存在
    exists = USER.objects.filter(username=username).exists()
    return Response({'exists': exists})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_email_exists(request):
    """
    检查邮箱是否已存在
    """
    email = request.GET.get('email', None)
    if not email:
        return Response({'error': '邮箱不能为空'}, status=status.HTTP_400_BAD_REQUEST)
    
    # 检查邮箱是否存在
    exists = USER.objects.filter(email=email).exists()
    return Response({'exists': exists})