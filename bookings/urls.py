from django.urls import path
from .views import home, booking_list ,booking_update , booking_create, booking_delete, register, user_login, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('booking/create/', home, name='booking_create'),
    path("bookings/", booking_list, name="booking_list"),
    path("bookings/new/", booking_create, name="booking_create"),
    path("bookings/edit/<int:booking_id>/", booking_update, name="booking_update"),
    path("bookings/delete/<int:booking_id>/", booking_delete, name="booking_delete"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
     path("contact/", contact_restaurant, name="contact_restaurant"),
]