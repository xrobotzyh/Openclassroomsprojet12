from rest_framework import permissions


class HasEventManipPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        connect_user = request.user
        if view.action == 'create':
            return connect_user.is_sales()
        else:
            return True

    def has_object_permission(self, request, view, obj):
        # only the contract associated client associated seller can create a event once the contract status is signed

        # only the assigned support personne or department of management can update the event
        connect_user = request.user
        if view.action in {'partial_update', 'update'}:
            return obj.assigned_to == connect_user.id or connect_user.is_management() or obj.client_id.contact_id == \
                connect_user.id
        if view.action in {'destroy'}:
            return connect_user.is_management()
        else:
            return True
