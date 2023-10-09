from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin

# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Client, Contract
# from .permissions import HasUserprofilePermissions
from .serializers import CreateContractSerializer


class CreateContratViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Contract.objects.all()
    serializer_class = CreateContractSerializer

    def perform_create(self, serializer):
        # user_id = self.request.user.id
        # client = Client.objects.all()
        contract = serializer.save()
        return contract


from django.shortcuts import render

# Create your views here.
