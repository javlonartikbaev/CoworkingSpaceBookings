from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsAdminUser, IsSimpleUser, IsManagerUser


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
