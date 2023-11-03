from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .filters import ContractFilter
from .models import Contract
from .permissions import HasContractManipPermissions
from .serializers import ContractSerializer


class ContratViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [IsAuthenticated, HasContractManipPermissions]
    pagination_class = PageNumberPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ContractFilter

