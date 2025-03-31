from django.shortcuts import render
from django.template.context_processors import request
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from users.permissions import IsAdminUser, IsSimpleUser, IsManagerUser


class TypeOfWorkingSpaceViewSet(ModelViewSet):
    queryset = TypeOfWorkingSpaces.objects.all()
    serializer_class = TypeOfWorkingSpacesSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            self.permission_classes = [IsManagerUser, IsAuthenticated]
        else:
            self.permission_classes = [IsSimpleUser, IsAdminUser]


class WorkingSpacesViewSet(ModelViewSet):
    queryset = WorkingSpaces.objects.all()
    serializer_class = WorkingSpacesSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            self.permission_classes = [IsManagerUser, IsAuthenticated]
        else:
            self.permission_classes = [IsSimpleUser, IsAdminUser]
