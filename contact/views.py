from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
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
        user_instance = self.request.user
        client_instance = serializer.save(contact_user=user_instance)
        return client_instance



from django.shortcuts import render

# Create your views here.
