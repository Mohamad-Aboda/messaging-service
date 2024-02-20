from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



# LOCAL IMPORT GOES HERE!
from .serializers import UserSerializer

""" Get user model """
User = get_user_model()

class CreateUserAPIView(APIView):
    """ Create user """
    permission_classes = (AllowAny, )

    @swagger_auto_schema(
        request_body=UserSerializer,
        operation_id="create_user",
        operation_summary="Register a new user"
    )
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class UserListView(APIView):
    """ List All users """
    @swagger_auto_schema(
        operation_summary="List all users"
    )
    def get(self, request):
        users = User.objects.all()
        if not users:
            return Response({'message': 'No users found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UserRetriveUpdateAPIView(RetrieveUpdateAPIView):
    """ List and Update user """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_id="get_user",
        operation_summary="Get user information"
    )
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UserSerializer,
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_id="update_user",
        operation_summary="Update user information"
    )
    def put(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(request.user, data=serializer_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=UserSerializer,
        manual_parameters=[
            openapi.Parameter(
                name="Authorization",
                in_=openapi.IN_HEADER,
                type=openapi.TYPE_STRING,
                description="Bearer token: 'Bearer {token}'",
            ),
        ],
        operation_id="partial_update_user",
        operation_summary="Partially update user information"
    )
    def patch(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer = self.serializer_class(request.user, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)




