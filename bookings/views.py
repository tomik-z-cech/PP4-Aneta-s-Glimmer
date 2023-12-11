from django.http import JsonResponse
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
    form_class = CreateBookingForm
    success_url = "/success/"  # Replace with your actual success URL

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "new_booking_form": CreateBookingForm(),
            },
        )

    def booking_options(request):
        selected_value = request.GET.get("selected_value", None)
        field_name = request.GET.get("field_name", None)
        if field_name == "#id_booked_style":
            options = ["Option 1", "Option 2", "Option 3"]
            data = {"next": "#id_booked_artist", "options": options}
        elif field_name == "#id_booked_artist":
            options = ["Option 1", "Option 2", "Option 3"]
            data = {"next": "#id_date"}
        return JsonResponse(data)

    def form_valid(self, form):
        # Handle form submission and save data
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        return self.form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
