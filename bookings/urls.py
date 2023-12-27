# PEP8
# Imports
from django.contrib.auth.decorators import login_required
from django.urls import path
from bookings import views


urlpatterns = [
    path("", views.MyBookingsView.as_view(), name="my-bookings"),
    path("new/", views.NewBookingView.as_view(), name="new-booking"),
    path(
        "booking-options/",
        login_required(views.BookingOptionsView.booking_options),
        name="booking-options",
    ),
    path(
        "cancel-request/<int:request_booking_pk>",
        login_required(views.MyBookingsView.cancel_request),
        name="cancel-request",
    ),
    path(
        "cancel-booking/<int:cancel_booking_pk>/",
        views.CancelBookingView.as_view(),
        name="cancel-booking",
    ),
    path(
        "rate-booking/<int:rate_booking_pk><int:score>/",
        views.RateBookingView.as_view(),
        name="rate-booking",
    ),
    path(
        "edit/<int:edit_booking_pk>",
        views.EditBookingView.as_view(),
        name="edit-booking",
    ),
]
