from rest_framework import serializers
from .models import USER
from django.contrib.auth.password_validation import validate_password


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


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    """用户创建与更新序列化器"""
    password = serializers.CharField(
        write_only=True,
        required=False,
        validators=[validate_password]
    )
    current_password = serializers.CharField(
        write_only=True,
        required=False
    )

    class Meta:
        model = USER
        fields = [
            'id', 'username', 'password', 'full_name', 'email', 'phone',
            'is_active', 'is_staff', 'is_superuser', 'date_joined',
            'last_login', 'created_by', 'current_password'
        ]
        read_only_fields = ['id', 'date_joined', 'last_login', 'created_by']

    def create(self, validated_data):
        # 密码加密存储
        if 'password' in validated_data:
            password = validated_data.pop('password')
            user = USER.objects.create_user(**validated_data)
            user.set_password(password)
            user.save()
        else:
            user = USER.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # 处理密码更新
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        
        # 移除current_password，因为它不应该是用户模型的字段
        validated_data.pop('current_password', None)
        
        return super().update(instance, validated_data)

    def validate(self, data):
        # 权限字段验证
        request = self.context.get('request')
        if not request:
            return data

        # 非超级管理员不能设置管理员权限
        if not request.user.is_superuser:
            if 'is_superuser' in data and data['is_superuser']:
                raise serializers.ValidationError({"permission": "没有权限设置超级管理员"})
            if 'is_staff' in data and data['is_staff']:
                raise serializers.ValidationError({"permission": "没有权限设置管理员"})

            # 确保普通管理员创建的用户不能是管理员
            if request.method == 'POST' and ('is_superuser' in data or 'is_staff' in data):
                if data.get('is_superuser', False) or data.get('is_staff', False):
                    raise serializers.ValidationError({"permission": "没有权限创建管理员用户"})
        
        return data