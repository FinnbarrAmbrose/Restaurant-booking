from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link booking to a user
    date = models.DateField()  # Booking date
    time = models.TimeField()  # Booking time
    guests = models.PositiveIntegerField()  # Number of guests
    created_at = models.DateTimeField(auto_now_add=True)  # Auto timestamp when created

    def __str__(self):
        return f"{self.date.strftime('%a %d %b')} at {self.time.strftime('%I:%M %p')} — {self.guests} guests"

class ContactMessage(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    dietary_preferences = models.CharField(max_length=255, blank=True)
    additional_notes = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for Booking #{self.booking.id}"