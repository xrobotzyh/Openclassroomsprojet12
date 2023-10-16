from rest_framework import permissions


class HasUserProfilePermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        connect_user = request.user
        if view.action == 'create':
            return connect_user.is_management()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        connected_user = request.user
        if view.action in {'destroy', 'partial_update', 'update'}:
            return connected_user.is_management()
        else:
            return True
