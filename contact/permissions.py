from rest_framework import permissions


class HasClientManipPermissions(permissions.BasePermission):
    """
    Client
    create: department management, department sales
    read: all registered users
    update: department management, sales(client was created by)
    delete: department management
    """
    def has_permission(self, request, view):
        connected_user = request.user
        if view.action == 'create':
            return connected_user.is_sales()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        connected_user = request.user
        if view.action in {'partial_update', 'update'}:
            return connected_user.is_management() or obj.contact == connected_user
        elif view.action == 'destroy':
            return connected_user.is_management()
        else:
            return True
