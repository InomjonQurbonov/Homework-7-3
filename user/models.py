from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=250,unique=True)
    email = models.EmailField()
    birth_date = models.DateField(blank=True, null=True)

    REQUIRED_FIELDS = [email,username]
