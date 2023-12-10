from django.urls import path
from bookings import views


urlpatterns = [
    path("", views.MyBookingsView.as_view(), name="my-bookings"),
]
