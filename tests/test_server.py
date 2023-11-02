import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from contact.models import Client
from user.models import User


@pytest.mark.django_db
def test_can_create_user_as_management(api_client, logged_as_management, create_user_data):
    token = logged_as_management
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.post('/api/users/', headers=headers, data=create_user_data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_can_not_create_user_as_not_management(api_client, logged_as_sales, create_user_data):
    token = logged_as_sales
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.post('/api/users/', headers=headers, data=create_user_data, format='json')

    assert response.status_code == 403


@pytest.mark.django_db
def test_can_get_client_as_sale(api_client, logged_as_sales):
    token = logged_as_sales
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.get('/api/clients/', headers=headers)

    assert response.status_code == 200


@pytest.mark.django_db
def test_can_get_client_as_support(api_client, logged_as_support):
    token = logged_as_support
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.get('/api/clients/', headers=headers)

    assert response.status_code == 200


@pytest.mark.django_db
def test_can_create_client_as_sales(api_client, logged_as_sales, create_client_data):
    token = logged_as_sales
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.post('/api/clients/', headers=headers, data=create_client_data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_can_create_client_as_not_sales(api_client, logged_as_support, create_client_data):
    token = logged_as_support
    headers = {'Authorization': f'Bearer {token}'}

    response = api_client.post('/api/clients/', headers=headers, data=create_client_data, format='json')

    assert response.status_code == 403


@pytest.mark.django_db
def test_can_create_contract_as_management(api_client, logged_as_management, create_client, create_contract_data):
    token = logged_as_management
    headers = {'Authorization': f'Bearer {token}'}
    client = create_client

    create_contract_data['client'] = client.id

    response = api_client.post('/api/contracts/', headers=headers, data=create_contract_data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_can_create_event_as_sales(api_client, logged_as_sales, create_contract, create_events_data,):
    user = User.objects.get(username='sale5')
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {token}'}
    contrat = create_contract

    create_events_data['contrat'] = contrat.id

    response = api_client.post('/api/events/', headers=headers, data=create_events_data, format='json')

    assert response.status_code == 201
