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
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        guests = cleaned_data.get('guests')

        if not booking_date or not guests:
            return cleaned_data 

        if booking_date < date.today():
            self.add_error('date', "You cannot book a table in the past. insted look to the future.")
            return cleaned_data

        # 1 table per booking
        total_tables_booked = Booking.objects.filter(date=booking_date).count()
        if total_tables_booked >= 10:
            raise ValidationError("Sorry, we are to put popularon on this day. Please select another day.")

        
        return cleaned_data

    def clean(self):
        booking_date = self.cleaned_data.get('date')

        
            
        existing_bookings = Booking.objects.filter(date=booking_date).count()
        if existing_bookings >= 10:
            raise ValidationError("Sorry, we are to put popularon this day. Please select another day.")


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