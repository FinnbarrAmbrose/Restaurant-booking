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
        return f"{self.date.strftime('%a %d %b')} at {self.time.strftime('%I:%M %p')} — {self.guests} guests"

class Meta:  
        ordering = ['date', 'time'] 

class ContactMessage(models.Model):
    booking = models.OneToOneField('Booking', on_delete=models.CASCADE)
    dietary_preferences = models.CharField(max_length=255)
    additional_notes = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for Booking #{self.booking.id}"