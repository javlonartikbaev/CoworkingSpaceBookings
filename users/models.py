from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        USER = 'user', 'Пользователь'
        MANAGER = 'manager', 'Менеджер'

    role = models.CharField(max_length=20,
                            choices=Roles.choices,
                            default=Roles.USER)

    image = models.ImageField(upload_to='users/', null=True, blank=True)
