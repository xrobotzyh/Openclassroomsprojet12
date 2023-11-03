import pytest
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from contact.models import Client
from contrat.models import Contract
from user.models import User


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def create_user():
    """
    a fixture return a user instance and will delete it after every use
    """
    user = User.objects.create_user(username='sale5', password='123456789', department='sales')
    yield user
    user.delete()


@pytest.fixture
def create_client(create_user):
    """
    a fixture that return client instance and will delete it after every use
    """
    user = create_user
    client = Client.objects.create(first_name='le', last_name='son', email='leson@447.fr', phone='325844',
                                   company_name='ooo', contact_id=user.id)
    yield client
    client.delete()


@pytest.fixture
def create_contract(create_client):
    """
    a fixture that return contract instance and will delete it after every use
    """
    client = create_client
    contract = Contract.objects.create(client=client, quotation='70', paid='0', status='sign')
    yield contract
    contract.delete()


@pytest.fixture
def logged_as_sales():
    """
    a fixture to create a user and get his token
    :return : user's token
    """
    user = User.objects.create_user(
        username='sale',
        password='123456789',
        department='sales'
    )
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token


@pytest.fixture
def logged_as_management():
    user = User.objects.create_user(
        username='mangement',
        password='123456789',
        department='management'
    )
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token


@pytest.fixture
def logged_as_support():
    user = User.objects.create_user(
        username='support',
        password='123456789',
        department='support'
    )
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    return token


@pytest.fixture
def create_user_data():
    """
    datas to be used to create a user
    :return: data informations
    """
    data = {
        'username': 'yy',
        'password': '123456789',
        'password2': '123456789',
        'phone': '123465',
        'department': 'sales'
    }
    return data


@pytest.fixture
def create_client_data():
    data = {
        'first_name': 'dididi',
        'last_name': "dududu",
        'email': '22@11.fr',
        'phone': '325844',
        'company_name': 'ooo'
    }
    return data


@pytest.fixture
def create_contract_data():
    data = {
        'client': 'null',
        'quotation': '100',
        'paid': '0',
        'status': 'sign'
    }
    return data


@pytest.fixture
def create_events_data():
    data = {
        "attendees": '7',
        "location": "lyon",
        "notes": "allez",
        "contrat": 'null'
    }
    return data
