# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
# from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated

from contact.models import Client
from user.models import User

from .models import Contract, Event
from .permissions import HasEventManipPermissions
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, HasEventManipPermissions]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ('assigned_to')

    def perform_create(self, serializer):
        contract_id = self.request.data.get('contrat')
        user_id = self.request.data.get('assigned_to')
        contrat = Contract.objects.get(id=contract_id)
        client = Client.objects.get(id=contrat.client_id)
        user = User.objects.get(id=user_id)
        event = serializer.save(client=client, assigned_to=user)
        return event

    def perform_update(self, serializer):
        serializer.save(assigned_to=self.request.data['assigned_to'])
