from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated

from .models import Client, Contract
from .permissions import HasContractManipPermissions
# from .permissions import HasUserprofilePermissions
from .serializers import ContractSerializer


class ContratViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, HasContractManipPermissions]

