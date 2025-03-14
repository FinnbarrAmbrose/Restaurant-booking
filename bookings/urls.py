from django.urls import path
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('booking/create/', home, name='booking_create'),
]