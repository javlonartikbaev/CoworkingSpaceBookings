from rest_framework.serializers import ModelSerializer
from .models import *


class TypeOfWorkingSpacesSerializer(ModelSerializer):
    class Meta:
        model = TypeOfWorkingSpaces
        fields = '__all__'


class WorkingSpacesSerializer(ModelSerializer):
    class Meta:
        model = WorkingSpaces
        fields = '__all__'
