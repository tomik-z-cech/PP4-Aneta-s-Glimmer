from django.urls import path
from bookings import views


urlpatterns = [
    path("", views.MyBookingsView.as_view(), name="my-bookings"),
    path("new/", views.NewBookingView.as_view(), name="new-booking"),
]
