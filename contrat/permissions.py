from rest_framework import permissions


class HasContractManipPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        connect_user = request.user
        if view.action in {'create', 'partial_update', 'update', 'destroy'}:
            return connect_user.is_management()
        else:
            return True
