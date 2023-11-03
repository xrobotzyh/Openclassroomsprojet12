from rest_framework import permissions, serializers

from contact.models import Client
from contrat.models import Contract


class HasEventManipPermissions(permissions.BasePermission):
    """
        Event
        create: department sales
        read: all registered users
        update: (department management, sales(which client was created by),department support(which assigned to),
                condition: contract status is signed
        delete: department management
    """

    def has_permission(self, request, view):
        # when action is create,firstly verifier is connected user is sales,if so, verifier if the sale user is the
        # user who created the client with whom events associated contract is associated to. if connected user is not
        # sales,no permissions assign
        connect_user = request.user
        if view.action == 'create':
            if connect_user.is_sales():
                contract_id = request.data.get('contrat')
                if contract_id is None:
                    # As i use drf framework api ui to test the function, i do not have post option once contract
                    # instance is none, in order to have post option, i must return true here
                    return True
                else:
                    try:
                        contract = Contract.objects.get(id=contract_id)
                        client = Client.objects.get(id=contract.client_id)
                        if client.contact != connect_user:
                            raise serializers.ValidationError('You do not have permission to create the event')
                    except (Contract.DoesNotExist, Client.DoesNotExist):
                        # if the contract or client doesn't exist
                        raise serializers.ValidationError('Invalid contract or client')
            else:
                return False
        return True

    def has_object_permission(self, request, view, obj):
        # only the contract associated client associated seller can create a event once the contract status is signed
        # only the assigned support personne or department of management can update the event
        connected_user = request.user
        if view.action in {'partial_update', 'update'}:
            return obj.assigned_to == connected_user or connected_user.is_management() or \
                Client.objects.get(id=obj.client_id).contact == connected_user
        if view.action in {'destroy'}:
            return connected_user.is_management()
        else:
            return True
