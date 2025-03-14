from django.shortcuts import render
from .models import Booking


def home(request):
    return render(request, "bookings/home.html")
