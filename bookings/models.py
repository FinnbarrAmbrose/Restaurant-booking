from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{
            self.date.strftime('%a %d %b')} at {
            self.time.strftime('%I:%M %p')} — {
            self.guests} guests"


class Meta:
    ordering = ['date', 'time']


class ContactMessage(models.Model):
    booking = models.ForeignKey(
        'bookings.Booking',
        on_delete=models.CASCADE,
        related_name='contact_messages'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contact_messages'
    )
    dietary_preferences = models.TextField()
    additional_notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Special request for {self.booking} by {self.user}"
