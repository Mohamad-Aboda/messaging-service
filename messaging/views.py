from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema



from .permissions import IsOwner
from .models import UserMessage
from .serializers import UserMessageSerializer
# from users.serializers import UserLogSerializer



""" Get user model """
User = get_user_model()

class InboxMessagesView(APIView):
    """ Get inbox messages for the authenticated user. """
    permission_classes = [IsOwner]


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_summary="Get Inbox Messages",
        operation_description="Retrieve all messages in the inbox of the authenticated user."
    )
    def get(self, request):
        user = request.user
        msgbox = UserMessage.objects.filter(to_user=user)
        serializer = UserMessageSerializer(msgbox, many=True)

        if not msgbox:
            return Response({'message': 'No messages in the inbox.'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data, status=status.HTTP_200_OK)

class OutboxMessagesView(APIView):
    """ Get outbox messages for the authenticated user."""

    permission_classes = [IsOwner]


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_summary="Get Outbox Messages",
        operation_description="Retrieve all messages in the outbox of the authenticated user."
    )
    def get(self, request):
        user = request.user
        msgbox = UserMessage.objects.filter(from_user=user)
        serializer = UserMessageSerializer(msgbox, many=True)

        if not msgbox:
            return Response({'message': 'No messages in the outbox.'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class SendMessageView(APIView):
    permission_classes = [IsOwner]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'receiver_username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the recipient'),
                'text': openapi.Schema(type=openapi.TYPE_STRING, description='Text of the message'),
            },
            required=['receiver_username', 'text'],
        ),
        responses={
            status.HTTP_201_CREATED: openapi.Response('Message sent successfully', UserMessageSerializer),
            status.HTTP_400_BAD_REQUEST: "Bad Request",
        },
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_summary="Send Message",
        operation_description="Send a message to a registered user with the specified username."
    )
    def post(self, request):
        sender_user = request.user
        receiver_username = request.data.get('receiver_username')
        if receiver_username is not None:
            try:
                receiver_user = User.objects.get(username=receiver_username)
            except User.DoesNotExist:
                return Response({'receiver_username': ["User not found."]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'receiver_username': ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        text = request.data.get('text')
        if not receiver_username:
            return Response({'receiver_username': ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        if not text:
            return Response({'text': ["This field is required."]}, status=status.HTTP_400_BAD_REQUEST)

        if not User.objects.filter(username=receiver_username).exists():
            return Response({'receiver_username': ["User should be exist."]}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            'from_user': sender_user.pk,
            'to_user': receiver_username,
            'message': {
                'content': request.data.get('text')
            }
        }
        user_msg_serializer = UserMessageSerializer(data=data)
        if not user_msg_serializer.is_valid():
            return Response(user_msg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:user_msg_serializer.save(to_user=receiver_user, from_user=sender_user)
            
        # log = {'user': sender_user.id,'action': "send"}
        # log_serializer = UserLogSerializer(data=log)
        # if not log_serializer.is_valid():return Response(log_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # else:log_serializer.save()

        return Response({'success': True,'message': 'Message sent successfully'}, status=status.HTTP_201_CREATED)

