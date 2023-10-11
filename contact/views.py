from uuid import uuid4

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from user.models import User
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Client
# from .permissions import HasUserprofilePermissions
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        uuid = uuid4()
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        client = serializer.save(contact_id=user, id=uuid)
        return client

# Create your views here.
