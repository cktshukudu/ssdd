from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    
    email = models.CharField(unique=True,max_length=60)
    password = models.CharField(max_length=150)
      
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []