from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link booking to a user
    date = models.DateField()  # Booking date
    time = models.TimeField()  # Booking time
    guests = models.PositiveIntegerField()  # Number of guests
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created
