import pytest
from rest_framework.exceptions import ErrorDetail


@pytest.mark.django_db
def test_create_ad(client, jwt_token):
    post_data = {
        'id': 100,
        'name': 'Test up to 10 symbols',
        'price': 1000,
        'description': 'test desc',
        'is_published': False
    }

    expected_response = {
        "id": 100,
        "is_published": False,
        "name": "Test up to 10 symbols",
        "price": 1000,
        "description": "test desc",
        "image": "http://testserver/logos/logo.png"
    }

    response = client.post(path='/ads/create/', data=post_data, HTTP_AUTHORIZATION=f'Bearer {jwt_token}')

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_no_auth(client):
    post_data = {
        'id': 100,
        'name': 'Test up to 10 symbols',
        'price': 1000,
        'description': 'test desc',
        'is_published': False
    }

    expected_response = {
        'detail': ErrorDetail(string='Authentication credentials were not provided.', code='not_authenticated')}

    response = client.post(path='/ads/create/', data=post_data)

    assert response.status_code == 401
    assert response.data == expected_response
