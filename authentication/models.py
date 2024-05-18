from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    company_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='user')
    phone_number = models.IntegerField(null=True,blank=True)
