from rest_framework import permissions

from utils.permissions import is_sales


class HasClientManipPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.action == 'create':
            print(is_sales(request.user.id))
            return is_sales(request.user.id)
        if view.action in {'partial_update', 'update'}:
            return obj.contact_id.id == request.user.id
        else:
            return True
