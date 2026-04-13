from django.contrib.auth.models import AbstractUser
from django.db import models
from shared.models import BaseModel

class CustomUser(BaseModel, AbstractUser):
    photo = models.ImageField(upload_to='users/', blank=True, null=True)
    phone_number = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username