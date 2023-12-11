from django.shortcuts import render, redirect
from django.views import generic
from bookings.models import Bookings
from bookings.forms import CreateBookingForm


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
        return render(
            request,
            self.template_name,
            {
                "new_booking_form": CreateBookingForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        return redirect("my-bookings")
