from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Custom user model extending AbstractUser.

    Attributes:
        email (EmailField): The unique email address of the user.
        avatar (ImageField): The path to the user's avatar image.
        country (CharField): The country of the user.
        phone (CharField): The phone number of the user.
    """

    username = None

    email = models.EmailField(unique=True, verbose_name='email')

    avatar = models.ImageField(upload_to='users_avatar/', verbose_name='avatar', **NULLABLE)
    country = models.CharField(max_length=40, verbose_name='country', **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name='phone', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
