from rest_framework import permissions

from utils.permissions import is_management


class HasContractManipPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action in {'create', 'partial_update', 'update'}:
            return is_management(request.user.id) or obj.client_id.contact_id.id == request.user.id
        if view.action in {'list', 'retrieve'}:
            return True
        else:
            return False
