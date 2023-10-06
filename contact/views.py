from uuid import uuid4

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from user.models import User
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Client
# from .permissions import HasUserprofilePermissions
from .serializers import CreateClientSerializer


class CreateClientViewSet(CreateModelMixin, viewsets.GenericViewSet):
    # give the queryset and serializer
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer

    def perform_create(self, serializer):
        uuid = uuid4()
        user_id = self.request.user.id
        print(user_id)
        user_instance = User.objects.get(id=user_id)
        client_instance = serializer.save(contact_user=user_instance, id=uuid)
        return client_instance


# Create your views here.
