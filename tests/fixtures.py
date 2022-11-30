import pytest


@pytest.fixture
@pytest.mark.django_db
def jwt_token(client, django_user_model):
    admin = {'id': 999,
             'username': 'test_admin',
             'email': 'admin@test.com',
             'password': 'test_admin_password',
             'age': 20}

    django_user_model.objects.create_user(**admin)

    response = client.post(path='/user/login/',
                           data={'username': admin['username'], 'password': admin['password']},
                           format='json')

    return response.data['access']
