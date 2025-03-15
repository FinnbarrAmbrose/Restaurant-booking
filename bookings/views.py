from django.shortcuts import render



def home(request):
    return render(request, "bookings/home.html")


def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('date', 'time')
    return render(request, "bookings/booking_list.html", {"bookings": bookings})



