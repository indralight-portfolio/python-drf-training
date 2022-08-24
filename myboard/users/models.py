from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=50, null=True)
    subjects = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to="profile/", default="default.png")
