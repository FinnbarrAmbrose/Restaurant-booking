from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.contrib import messages
from .forms import UserRegisterForm, ContactMessageForm
from .models import Booking, ContactMessage


def home(request):
    return render(request, "bookings/home.html")


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(
        user=request.user).order_by(
        "date", "time")
    return render(request,
                  "bookings/booking_list.html",
                  {"bookings": bookings})


@login_required
def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Assign booking to the logged-in user
            booking.save()
            messages.success(request, "Booking successfully created!")
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
            messages.success(request, "Booking successfully updated!")
            return redirect("booking_list")  # Redirect to booking list
    else:
        form = BookingForm(instance=booking)

    return render(request, "bookings/booking_form.html", {"form": form})


@login_required
def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking successfully cancelled.")
        return redirect("booking_list")  # Redirect to booking list

    return render(request,
                  "bookings/booking_confirm_delete.html",
                  {"booking": booking})


@login_required
def contact_restaurant(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if ContactMessage.objects.filter(
            booking=booking,
            user=request.user).exists():
        messages.warning(
            request,
            "You have already submitted a special request for this booking.")
        return redirect("booking_list")

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.booking = booking
            message.user = request.user
            message.save()
            messages.success(request, "Your special request has been sent.")
            return redirect("booking_list")
    else:
        form = ContactMessageForm()

    return render(request, "bookings/contact_restaurant.html", {
        "form": form,
        "booking": booking,
    })


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(
                request,
                f"Welcome {username}, your account was created successfully!")
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
