from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date
from django.db.models import Sum


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 4}), # Limit the guests to 4 
        }

 # guest count (1 to 4 )
    def clean_guests(self):
        guests = self.cleaned_data.get('guests')
        if guests < 1 or guests > 4:
            raise ValidationError("Each table is only allowed 1 to 4 guests.")
        return guests
        
    def clean(self):
        booking_date = self.cleaned_data.get('date')

        if booking_date < date.today():
            raise ValidationError("You cannot book a table in the past. insted look to the future.")
            
        existing_bookings = Booking.objects.filter(date=booking_date).count()
        if existing_bookings >= 10:
            raise ValidationError("Sorry, we are Two put popularon this day. Please select another day.")


        return booking_date

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})