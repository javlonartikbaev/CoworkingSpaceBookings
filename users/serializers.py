from django.core.validators import MinLengthValidator
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[MinLengthValidator(8)])

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'image', 'role']
