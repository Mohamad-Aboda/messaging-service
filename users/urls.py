from django.urls import path 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateUserAPIView, UserRetriveUpdateAPIView, UserListView

app_name = 'users'
urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='register-user'),
    path('list-update/', UserRetriveUpdateAPIView.as_view(), name='update-user'),
    path('all-users/', UserListView.as_view(), name='user-list'),



    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token

]