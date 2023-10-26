import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from user.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def create_sale_user():
    user = User.objects.create_user(
        username='sale',
        password='123456789'
    )
    return user


def create_manage_user():
    user = User.objects.create_user(
        username='mangement',
        password='123456789'
    )
    return user


def create_support_user():
    user = User.objects.create_user(
        username='support',
        password='123456789'
    )
    return user


@pytest.fixture
def get_sale_token(create_sale_user):
    user = create_sale_user
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token


@pytest.fixture
def get_manage_token(create_manage_user):
    user = create_manage_user
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token


@pytest.fixture
def get_support_token(create_support_user):
    user = create_support_user
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token
