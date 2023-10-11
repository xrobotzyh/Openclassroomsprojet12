from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # give the queryset and serializer
    queryset = User.objects.all()
    serializer_class = UserSerializer

