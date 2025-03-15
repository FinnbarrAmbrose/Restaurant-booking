from django.shortcuts import render



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