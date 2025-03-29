from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
from .managers import UserManager


class User(AbstractBaseUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        USER = 'user', 'Пользователь'
        MANAGER = 'manager', 'Менеджер'

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=8)
    image = models.ImageField(upload_to='users/', null=True, blank=True)
    role = models.CharField(max_length=20,
                            choices=Roles.choices,
                            default=Roles.USER)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f'{self.email} - {self.role}'

    class Meta:
        db_table = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
