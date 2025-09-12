from rest_framework import permissions


class IsSuperuserOrStaff(permissions.BasePermission):
    """仅超级管理员或管理员可访问"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_superuser or request.user.is_staff
        )


class IsSuperuser(permissions.BasePermission):
    """仅超级管理员可访问"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsOwnerOrAdmin(permissions.BasePermission):
    """本人、超级管理员或管理员可访问"""
    def has_object_permission(self, request, view, obj):
        # 本人可访问
        if request.user == obj:
            return True
        # 管理员权限检查
        if request.user.is_superuser:
            return True
        if request.user.is_staff:
            # 管理员只能操作普通用户
            return not (obj.is_superuser or obj.is_staff)
        return False

