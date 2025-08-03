from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('rider', 'Rider'),
        ('driver', 'Driver'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_driver = models.BooleanField(default=False)
    is_rider = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
