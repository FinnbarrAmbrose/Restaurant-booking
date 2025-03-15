from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm


def home(request):
    return render(request, "bookings/home.html")


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, "bookings/booking_list.html", {"bookings": bookings})




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


def booking_delete(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if request.method == "POST":
        booking.delete()
        return redirect("booking_list")  # Redirect to booking list

    return render(request, "bookings/booking_confirm_delete.html", {"booking": booking})