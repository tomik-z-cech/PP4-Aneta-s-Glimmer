from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from bookings.models import Bookings
from bookings.forms import CreateBookingForm
from styles.models import StylesAvailable
from artists.models import Artists


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
        options = []
        selected_value = request.GET.get("selected_value", None)
        field_name = request.GET.get("field_name", None)
        if field_name == "#id_booked_style":
            artists_with_style = Artists.objects.filter(styles__in=[selected_value]).order_by("-rating")
            for artist in artists_with_style:
                rating_string = str(artist.rating)
                options.append(artist.name + " - Rating : " + rating_string)
            data = {"options": options}
        elif field_name == "#id_date":
            options = ["Option 1", "Option 2", "Option 3"]
            data = {"options": options}
        return JsonResponse(data)

    def form_valid(self, form):
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
