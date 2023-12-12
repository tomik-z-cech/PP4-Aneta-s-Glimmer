from django.urls import path
from bookings import views


urlpatterns = [
    path("", views.MyBookingsView.as_view(), name="my-bookings"),
    path("new/", views.NewBookingView.as_view(), name="new-booking"),
    path('booking-options/', views.NewBookingView.booking_options, name='booking-options'),
    path('cancel/<int:pk>', views.CancelBookingView.as_view(), name='cancel-booking'),
    
]
