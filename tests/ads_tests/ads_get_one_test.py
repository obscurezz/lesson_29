import pytest


@pytest.mark.django_db
def test_retrieve_one_ad(client, ad, jwt_token):
    expected_response = {
        'id': ad.pk,
        'author': ad.author,
        'category': ad.category,
        'name': ad.name,
        'price': ad.price,
        'description': ad.description,
        'is_published': False,
        'image': 'http://testserver/logos/logo.png',
    }

    response = client.get(f'/ads/{ad.pk}/', HTTP_AUTHORIZATION=f'Bearer {jwt_token}')

    assert response.status_code == 200
    assert response.data == expected_response
