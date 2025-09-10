from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

USER = get_user_model()

class SHA256PasswordBackend:
    """
    自定义认证后端：
    - 接收前端 SHA-256 加密后的密码
    - 使用该 SHA-256 值作为“明文”进行 Django PBKDF2 验证
    """
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None

        try:
            user = USER.objects.get(username=username)
        except USER.DoesNotExist:
            # 保持与原逻辑一致，避免信息泄露
            return None

        if not user.is_active:
            return None

        # 关键：使用前端传来的 SHA-256 密码作为“明文”验证
        if check_password(password, user.password):
            return user

        return None

    def get_user(self, user_id):
        try:
            return USER.objects.get(pk=user_id)
        except USER.DoesNotExist:
            return None