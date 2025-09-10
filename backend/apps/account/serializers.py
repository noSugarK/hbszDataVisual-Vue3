from rest_framework import serializers
from apps.users.models import USER

class UserDetailSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = USER
        fields = [
            'id', 'username', 'first_name', 'is_superuser',
            'is_staff', 'permissions'
        ]

    def get_permissions(self, obj):
        # 示例权限结构（可根据实际 RBAC 扩展）
        return {
            "projects": [],
            "regions": []
        }

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)