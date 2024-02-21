from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from rest_framework import serializers


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(
        write_only=True,
        validators=[MinLengthValidator(limit_value=4, message="Password must be at least 3 characters.")]
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)



