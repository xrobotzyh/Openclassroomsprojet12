from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from contact.models import Client
from user.models import User
from .filters import EventFilter

from .models import Contract, Event
from .permissions import HasEventManipPermissions
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, HasEventManipPermissions]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = EventFilter

    def perform_create(self, serializer):
        contract_id = self.request.data.get('contrat')
        user_id = self.request.data.get('assigned_to')

        contrat = Contract.objects.get(id=contract_id)
        client = Client.objects.get(id=contrat.client_id)
        user = User.objects.get(id=user_id)

        event = serializer.save(client=client, assigned_to=user)
        return event

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.data['assigned_to'])
        serializer.save(assigned_to=user)
