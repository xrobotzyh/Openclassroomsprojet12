from uuid import uuid4

from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

from user.models import User
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Client, Contract
# from .permissions import HasUserprofilePermissions
from .serializers import CreateContractSerializer


class CreateContratViewSet(CreateModelMixin, viewsets.GenericViewSet):
    # give the queryset and serializer
    queryset = Contract.objects.all()
    serializer_class = CreateContractSerializer

    def perform_create(self, serializer):
        uuid = uuid4()
        # user_id = self.request.user.id
        # client = Client.objects.all()
        contract_instance = serializer.save(id=uuid)
        return contract_instance


from django.shortcuts import render

# Create your views here.
