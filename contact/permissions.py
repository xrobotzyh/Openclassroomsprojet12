from rest_framework import permissions


class HasClientManipPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        connect_user = request.user
        if view.action == 'create':
            return connect_user.is_sales()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        connect_user = request.user
        if view.action in {'partial_update', 'update'}:
            return connect_user.is_management() or obj.contact.id == connect_user.id
        elif view.action == 'destroy':
            return connect_user.is_management()
        else:
            return True
