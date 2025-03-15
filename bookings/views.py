from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from django.contrib import messages 


def home(request):
    return render(request, "bookings/home.html")

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, "bookings/booking_list.html", {"bookings": bookings})



@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign booking to the logged-in user
            booking.save()
            return redirect("booking_list")  # Redirect to booking list
    else:
        form = BookingForm()
    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def booking_update(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect("booking_list")  # Redirect to booking list
    else:
        form = BookingForm(instance=booking)

    return render(request, "bookings/booking_form.html", {"form": form})

@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect("booking_list")  # Redirect to booking list

    return render(request, "bookings/booking_confirm_delete.html", {"booking": booking})


# Login and registration views
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
 
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("home")
    else:
        form = UserRegisterForm()
    return render(request, "bookings/register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
           messages.error(request, "Invalid username or password")
    return render(request, "bookings/login.html")

def user_logout(request):
    logout(request)
    return redirect("home")
    