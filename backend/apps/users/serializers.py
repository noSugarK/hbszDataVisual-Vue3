from rest_framework import serializers
from .models import USER


class UserProfileSerializer(serializers.ModelSerializer):
    """
    用户个人信息序列化器
    """
    class Meta:
        model = USER
        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'phone',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login'
        ]
        read_only_fields = [
            'id',
            'username',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login'
        ]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化器（用于管理员查看）
    """
    class Meta:
        model = USER
        fields = [
            'id',
            'username',
            'full_name',
            'email',
            'phone',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'created_by'
        ]