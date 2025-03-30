from django.core.validators import MinLengthValidator
from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[MinLengthValidator(8)])

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'image', 'role', 'is_active']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
