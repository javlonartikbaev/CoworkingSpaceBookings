from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        return bool(request.user.role == 'admin')


class IsManagerUser(BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        return bool(request.user.role == 'manager')


class IsSimpleUser(BasePermission):
    message = 'You do not have permission to perform this action.'

    def has_permission(self, request, view):
        return bool(request.user.role == 'user')
