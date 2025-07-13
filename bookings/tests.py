import datetime

from django.test import TestCase
from django.contrib.auth.models import User

from .models import Booking
from .forms import ContactMessageForm


class BookingModelTest(TestCase):
    def setUp(self):
        # create a user and a booking for tomorrow at 18:00
        self.user = User.objects.create_user(
            username="tester", password="pass")
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=datetime.time(hour=18, minute=0),
            guests=2
        )

    def test_str_method(self):
        expected = (
            f"{self.booking.date.strftime('%a %d %b')} at "
            f"{self.booking.time.strftime('%I:%M %p')} — "
            f"{self.booking.guests} guests"
        )
        self.assertEqual(str(self.booking), expected)

    def test_default_ordering(self):
        # create a second booking at a later time on the same day
        later = Booking.objects.create(
            user=self.user,
            date=self.booking.date,
            time=datetime.time(hour=19, minute=0),
            guests=1
        )
        qs = list(Booking.objects.all())
        # should follow Meta.ordering = ['date', 'time']
        self.assertEqual(qs, [self.booking, later])


class ContactMessageFormTest(TestCase):
    def setUp(self):
        # need a booking for the form’s FK
        self.user = User.objects.create_user(username="joe", password="pass")
        self.booking = Booking.objects.create(
            user=self.user,
            date=datetime.date.today() + datetime.timedelta(days=1),
            time=datetime.time(hour=18, minute=0),
            guests=2
        )

    def test_empty_form_is_invalid(self):
        form = ContactMessageForm(data={})
        self.assertFalse(form.is_valid())
        # form should complain about both required text fields
        self.assertIn('dietary_preferences', form.errors)
        self.assertIn('additional_notes', form.errors)

    def test_valid_form_saves(self):
        data = {
            'dietary_preferences': 'Vegetarian',
            'additional_notes': 'No peanuts, please'
        }
        form = ContactMessageForm(data=data)
        self.assertTrue(form.is_valid())

        # mirror your view logic: commit=False, set booking & user, then save
        msg = form.save(commit=False)
        msg.booking = self.booking
        msg.user = self.user
        msg.save()

        # now all fields should be set correctly
        self.assertEqual(msg.dietary_preferences, 'Vegetarian')
        self.assertEqual(msg.additional_notes, 'No peanuts, please')
        self.assertEqual(msg.booking, self.booking)
        self.assertEqual(msg.user, self.user)
        self.assertIn(str(self.user), str(msg))
