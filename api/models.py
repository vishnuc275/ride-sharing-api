from django.db import models
from django.conf import settings

class Ride(models.Model):
    STATUS_CHOICES = [
        ('requested','Requested'),
        ('accepted','Accepted'),
        ('started','Started'),
        ('completed','Completed'),
        ('cancelled','Cancelled')
    ]

    rider = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="rides_requested", on_delete=models.CASCADE)
    driver= models.ForeignKey(settings.AUTH_USER_MODEL, related_name="drives",on_delete=models.SET_NULL, null=True, blank=True)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    current_location = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} {self.status}"