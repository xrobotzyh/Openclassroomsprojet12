from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import User
# from rest_framework.pagination import PageNumberPagination


from .models import Contract, Event
from .permissions import HasEventManipPermissions
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated, HasEventManipPermissions]

    def perform_create(self, serializer):
        contrat_id = self.request.data['contrat_id']
        user_id = self.request.data['assigned_to']
        contrat = Contract.objects.get(id=contrat_id)
        client_id = contrat.client_id
        user = User.objects.get(id=user_id)
        event = serializer.save(client_id=client_id, assigned_to=user)
        return event

    def perform_update(self, serializer):
        serializer.save(assigned_to_id=self.request.data['assigned_to'])

