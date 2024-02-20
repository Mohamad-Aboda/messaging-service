# messaging_service/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings
from .views import show_endpoints

schema_view = get_schema_view(
    openapi.Info(
        title="messaging service.",
        default_version="v1",
        description="messaging service.",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="muhammeed.abdelhameed@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", show_endpoints, name='show-all-available-endpoints'),
    path('admin/', admin.site.urls),
    path("api/v1/messaging/", include("messaging.urls", namespace="messaging")),
    path("api/v1/user/", include("users.urls", namespace="users")),

    # Swagger endpoints
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0),name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),name='schema-redoc'),
]