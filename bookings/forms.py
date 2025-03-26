from django import forms
from .models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from datetime import date

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'guests': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 4}), # Limit the guests to 4 
        }

        def clean_guests(self):
            guests = self.cleaned_data.get('guests')
            if guests < 1 or guests > 4:
                raise ValidationError("Each table must have between 1 and 4 guests.")
            return guests
        
        def clean_date(self):
            booking_date = self.cleaned_data.get('date')

            if booking_date < date.today():
                raise ValidationError("You cannot book a table in the past look to the future.")
            
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