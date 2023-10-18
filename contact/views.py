from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from user.models import User
from .filters import ContactFilter
from .models import Client
from .permissions import HasClientManipPermissions
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, HasClientManipPermissions]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ContactFilter
    ordering_filter_class = OrderingFilter

    def perform_create(self, serializer):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        client = serializer.save(contact=user)
        return client
