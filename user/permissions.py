from rest_framework import permissions

from utils.permissions import is_management


class HasUserProfilePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in {'create', 'destroy', 'partial_update', 'update'}:
            return is_management(request.user.id)
        else:
            return True
