from rest_framework.permissions import BasePermission

from authentication.models import User


class SelectionOwnerPermission(BasePermission):
    message = 'Only an owner can retrieve detail information'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner


class CreatedByPrivilegedUserPermission(BasePermission):
    message = 'Only an owner or a privileged user can modify or delete'

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN or request.user.role == User.MODERATOR:
            return True
        if obj.author == request.user:
            return True
        return False
