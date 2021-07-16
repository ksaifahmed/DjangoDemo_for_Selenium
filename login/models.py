from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, name=None, age=None, phone=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.name = name
        user.age = age
        user.phone = phone
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None

    name = models.TextField(max_length=100)
    phone = models.BigIntegerField(unique=True)
    age = models.IntegerField()
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email
