from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import User
# from rest_framework.pagination import PageNumberPagination
from .models import Client
from .permissions import HasClientManipPermissions
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated, HasClientManipPermissions]

    def perform_create(self, serializer):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        client = serializer.save(contact=user)
        return client

# Create your views here.
