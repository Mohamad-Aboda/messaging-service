from rest_framework.test import APIClient
from rest_framework import status
import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user_data():
    return {
        'username': 'testuser',
        'password': 'testpassword',
    }

@pytest.mark.django_db
def test_create_user(api_client, user_data):
    response = api_client.post(reverse('users:register-user'), user_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_retrieve_user(api_client, user_data):
    user = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=user)

    response = api_client.get(reverse('users:list-update'))
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_update_user(api_client, user_data):
    user = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=user)

    updated_data = {
        'username':'testuser2',
        'password': 'updatepassword'
    }

    response = api_client.put(reverse('users:list-update'), updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == updated_data['username']

@pytest.mark.django_db
def test_partial_update_user(api_client, user_data):
    user = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=user)

    updated_data = {
        'username': 'updated username',
    }

    response = api_client.patch(reverse('users:list-update'), updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == updated_data['username']
