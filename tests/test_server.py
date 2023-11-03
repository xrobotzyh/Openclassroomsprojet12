import pytest
from rest_framework_simplejwt.tokens import RefreshToken

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
def test_can_create_contract_as_not_management(api_client, logged_as_support, create_client, create_contract_data):
    """
    :param api_client: a django test client
    :param logged_as_support: create and login as support
    :param create_client: create a client instance by given param
    :param create_contract_data: data to be used to test to create a contract
    :return: status code give the divers informations

    the support department has no permission to create a contract
    """
    token = logged_as_support
    headers = {'Authorization': f'Bearer {token}'}
    client = create_client

    create_contract_data['client'] = client.id

    response = api_client.post('/api/contracts/', headers=headers, data=create_contract_data, format='json')

    assert response.status_code == 403


@pytest.mark.django_db
def test_can_create_event_as_sales(api_client, logged_as_management, create_contract, create_events_data, ):
    """
    :param api_client: a django test client
    :param logged_as_management: create and login as management
    :param create_contract: create a contract instance by given param
    :param create_events_data: data to be used to test to create a events
    :return: status code give the divers informations

    the sale can create a event only if the sale is the one who created the client with whom events associated contract
    is associated to.
    """
    user = User.objects.get(username='sale5')
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    headers = {'Authorization': f'Bearer {token}'}
    contrat = create_contract

    create_events_data['contrat'] = contrat.id

    response = api_client.post('/api/events/', headers=headers, data=create_events_data, format='json')

    assert response.status_code == 201


@pytest.mark.django_db
def test_can_create_event_as_not_sales(api_client, logged_as_management, create_contract, create_events_data, ):
    """
    :param api_client: a django test client
    :param logged_as_management: create and login as management
    :param create_contract: create a contract instance by given param
    :param create_events_data: data to be used to test to create a events
    :return: status code give the divers informations

    the management department has no permission to create a events
    """
    token = logged_as_management
    headers = {'Authorization': f'Bearer {token}'}
    contrat = create_contract

    create_events_data['contrat'] = contrat.id

    response = api_client.post('/api/events/', headers=headers, data=create_events_data, format='json')

    assert response.status_code == 403
