from rest_framework.test import APIClient
from rest_framework import status
import pytest

from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import UserMessage, Message

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

@pytest.fixture
def message_data():
    return {
        'text': 'Hello, testing!',
        'receiver_username': 'receiveruser',
    }

@pytest.mark.django_db
def test_send_message(api_client, user_data, message_data):
    sender = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=sender)

    receiver = User.objects.create_user(username=message_data['receiver_username'], password='receiverpassword')

    response = api_client.post(reverse('messaging:send_message'), message_data, format='json')
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_get_outbox(api_client, user_data, message_data):
    sender = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=sender)

    

    # Send a message
    _ = User.objects.create_user(username=message_data['receiver_username'], password='receiverpassword')
    api_client.post(reverse('messaging:send_message'), message_data, format='json')

    response = api_client.get(reverse('messaging:outbox_message'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1 



@pytest.mark.django_db
def test_get_inbox(api_client, user_data, message_data):
    sender = User.objects.create_user(**user_data)
    api_client.force_authenticate(user=sender)

    receiver = User.objects.create_user(username=message_data['receiver_username'], password='receiverpassword')
    api_client.post(reverse('messaging:send_message'), message_data, format='json')

    # Retrieve inbox messages for the receiver
    api_client.force_authenticate(user=receiver)
    response = api_client.get(reverse('messaging:inbox_message'))

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1