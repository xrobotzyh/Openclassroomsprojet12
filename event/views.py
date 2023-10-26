from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

        if contract_id is None:
            return Response({"error": "contract_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        if user_id is None:
            user = None
        else:
            user = User.objects.get(id=user_id)

        contrat = Contract.objects.get(id=contract_id)
        client = Client.objects.get(id=contrat.client_id)

        event = serializer.save(client=client, assigned_to=user)
        return event

    def perform_update(self, serializer):
        user = User.objects.get(id=self.request.data['assigned_to'])
        serializer.save(assigned_to=user)
