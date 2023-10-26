import pytest


@pytest.mark.django_db
def test_can_create_user_as_management(api_client, get_manage_token):
    token = get_manage_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = api_client.get('/api/users/')
    assert response.status_code == 200

    api_client.post('/api/users/', {'username': 'yy', 'password': '123456789'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_can_create_user_as_not_management(api_client, get_sale_token):
    token = get_sale_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = api_client.get('/api/users/')
    assert response.status_code == 200

    api_client.post('/api/users/', {'username': 'yy', 'password': '123456789'})
    assert response.status_code == 401


@pytest.mark.django_db
def test_can_read_client_as_sale(api_client, get_sale_token):
    token = get_sale_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = api_client.get('/api/clients/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_can_read_client_as_support(api_client, get_support_token):
    token = get_support_token
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    response = api_client.get('/api/clients/')
    assert response.status_code == 401
