import pytest
from rest_framework.exceptions import ErrorDetail

from tests.factories import AdFactory


@pytest.mark.django_db
def test_create_selection(client, jwt_token):
    ads = AdFactory.create_batch(3)
    items = [ad.pk for ad in ads]

    post_data = {
        "id": 1,
        "name": "new test selection 1",
        "owner": 999,
        "items": items
    }

    expected_response = {
        "id": 1,
        "name": "new test selection 1",
        "owner": 999,
        "items": items
    }

    response = client.post(path='/selection/create/', data=post_data, HTTP_AUTHORIZATION=f'Bearer {jwt_token}')

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_selection_no_auth(client):
    ads = AdFactory.create_batch(3)
    items = [ad.pk for ad in ads]

    post_data = {
        "id": 1,
        "name": "new test selection 1",
        "owner": 999,
        "items": items
    }

    expected_response = {
        'detail': ErrorDetail(string='Authentication credentials were not provided.', code='not_authenticated')}

    response = client.post(path='/selection/create/', data=post_data)

    assert response.status_code == 401
    assert response.data == expected_response
