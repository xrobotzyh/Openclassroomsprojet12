from rest_framework import permissions

from utils.permissions import is_management


class HasEventManipPermissions(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # only the contract associated client associated seller can create a event once the contract status is signed
        if view.action == 'create':
            return obj.client_id.contact_id.id == request.user.id and obj.contract_id.status == 'sign'
        # only the assigned support personne or department of management can update the event
        if view.action in {'partial_update', 'update'}:
            return obj.assigned_to == request.user.id or is_management(request.user.id)
        if view.action in {'list', 'retrieve'}:
            return True
        else:
            return False
