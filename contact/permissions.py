from rest_framework import permissions


class HasClientManipPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        connected_user = request.user
        if view.action == 'create':
            return connected_user.is_sales()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        connected_user = request.user
        if view.action in {'partial_update', 'update'}:
            return connected_user.is_management() or obj.contact.id == connected_user.id
        elif view.action == 'destroy':
            return connected_user.is_management()
        else:
            return True
