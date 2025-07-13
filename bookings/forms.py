from django import forms
from django.core.exceptions import ValidationError
from datetime import date, time
from .models import Booking, ContactMessage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

TIME_CHOICES = [
    (time(18, 0), '18:00 PM'),
    (time(19, 0), '19:00 PM'),
    (time(20, 0), '20:00 PM'),
    (time(21, 0), '21:00 PM'),
    (time(22, 0), '22:00 PM'),
    (time(23, 0), '23:00 PM'),
]


class ContactMessageForm(forms.ModelForm):
    """
    Form for users to submit dietary preferences and additional notes
    linked to a Booking.
    """

    class Meta:
        model = ContactMessage
        fields = ['dietary_preferences', 
                  'additional_notes']
        widgets = {
            'dietary_preferences': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': (
                        'E.g. Vegetarian, '
                        'Nut allergy'
                    )
                }
            ),
            'additional_notes': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': (
                        'Any special requirements '
                        'like wheelchair access'
                    )
                }
            ),
        }

    def clean(self):
        """ Ensure both fields are filled out (not blank or whitespace)."""
        cleaned_data = super().clean()

        if not cleaned_data.get('dietary_preferences', 
                                '').strip():
            self.add_error(
                'dietary_preferences',
                'Please enter your dietary preferences.'
            )
        if not cleaned_data.get('additional_notes',
                                 '').strip():
            self.add_error(
                'additional_notes',
                'Please enter additional notes.'
            )

        return cleaned_data

class BookingForm(forms.ModelForm):
    """
    Form to create or update a Booking instance:
    validates date (no past), time, and number of guests.
    """
    time = forms.ChoiceField(
        choices=TIME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Booking
        fields = ['date', 'time', 'guests']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 
                       'class': 'form-control'}
            ),
            'time': forms.TimeInput(
                attrs={'type': 'time', 
                       'class': 'form-control'}
            ),
            # Limit the guests to 1 to 4
            'guests': forms.NumberInput(
                attrs={'class': 'form-control', 
                       'min': 1,
                         'max': 4}
            ),
        }

    def clean_guests(self):
        """
        Ensure guests count is between 1 and 4 inclusive.
        """
        guests = self.cleaned_data.get('guests')
        if guests < 1 or guests > 4:
            raise ValidationError(
                "Each table is only allowed 1 to 4 guests."
            )
        return guests

    def clean(self):
        """
        Validate booking date (not in the past) 
        and capacity for the date.
        """
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('date')
        guests = cleaned_data.get('guests')

        if not booking_date or not guests:
            return cleaned_data

        if booking_date < date.today():
            self.add_error(
                'date',
                (
                    "You cannot book a table in the past. "
                    "Please select a future date."
                ),
            )
            return cleaned_data

        # Max 10 tables per day
        total_tables_booked = Booking.objects.filter(date=booking_date).count()
        if total_tables_booked >= 10:
            raise ValidationError(
                (
                    "Sorry, we are at capacity on this day. "
                    "Please select another date."
                )
            )

        return cleaned_data
        
class UserRegisterForm(UserCreationForm):
    """
    Form for user registration including email.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", 
                  "email", 
                  "password1", 
                  "password2"]

    def __init__(self, *args, **kwargs):
        """
        Add CSS classes to widgets.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})
