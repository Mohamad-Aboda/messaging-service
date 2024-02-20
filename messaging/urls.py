from django.urls import path
from .views import (InboxMessagesView, OutboxMessagesView, SendMessageView)

app_name = "messaging"

urlpatterns = [

    path('inbox/', InboxMessagesView.as_view(), name='inbox'),
    path('outbox/', OutboxMessagesView.as_view(), name='outbox'),
    path('send-message/', SendMessageView.as_view(), name='send_message'),
    
]
