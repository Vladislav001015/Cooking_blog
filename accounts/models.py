from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField('email address',unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.get_full_name()