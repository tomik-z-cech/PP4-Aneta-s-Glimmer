from django.shortcuts import render
from django.views import generic
from bookings.models import Bookings


class MyBookingsView(generic.ListView):
    template_name = "bookings/bookings.html"
    model = Bookings

    def get(self, request, *args, **kwargs):
        login_user = request.user
        user_bookings = Bookings.objects.filter(username=login_user)
        return render(
            request,
            self.template_name,
            {
                "bookings": user_bookings,
            },
        )
        
class NewBookingView(generic.ListView):
    template_name = "bookings/new_booking.html"
    model = Bookings
    
    def get(self, request, *args, **kwargs):
        login_user = request.user
        user_bookings = Bookings.objects.filter(username=login_user)
        return render(
            request,
            self.template_name,
            {
                "new_booking_form": user_bookings,
            },
        )
