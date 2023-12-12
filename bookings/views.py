from datetime import datetime
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from bookings.models import Bookings
from bookings.forms import CreateBookingForm
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
    form = CreateBookingForm
    success_url = "/bookings/"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "new_booking_form": CreateBookingForm(),
            },
        )

    def booking_options(request):
        booked_style_new = request.session.get("booked_style_new", None)
        booked_artist_new = request.session.get("booked_artist_new", None)
        received_value = request.GET.get("selected_value", None)
        field_name = request.GET.get("field_name", None)
        if field_name == "#id_booked_style":
            request.session["booked_style_new"] = received_value
            options = ['<option value="0" selected>Select Artist</option>']
            artists_with_style = Artists.objects.filter(
                styles__in=[received_value]
            ).order_by("-rating")
            for artist in artists_with_style:
                artist_id = str(artist.id)
                options.append(
                    '<option value="' + artist_id + '">' + artist.name + "</option>"
                )
            data = {"options": options}
        elif field_name == "#id_booked_artist":
            request.session["booked_artist_new"] = received_value
            data = {}
        elif field_name == "#id_date":
            options = ['<option value="0">Select Time</option>']
            booked_date_new = received_value
            bookings_artist = Bookings.objects.filter(
                booked_artist__in=[booked_artist_new]
            )
            bookings_artist_day = bookings_artist.filter(
                date_time__date=booked_date_new
            )
            time_range = [
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
            ]
            for i in time_range:
                match = 0
                for booking in bookings_artist_day:
                    if i == booking.date_time.time().strftime("%H:%M"):
                        match = 1
                if match == 0:
                    options.append('<option value="' + i + ':00">' + i + "</option>")
                else:
                    options.append(
                        '<option value="' + i + ':00" disabled>' + i + "</option>"
                    )
            data = {"options": options}
        return JsonResponse(data)

    def post(self, request, *args, **kwargs):
        booking_form = self.form(data=request.POST)
        if booking_form.is_valid():
            # print(request.POST)
            date_converted = datetime.strptime(request.POST["date"], "%Y-%m-%d").date()
            time_converted = datetime.strptime(request.POST["time"], "%H:%M:%S").time()
            booking_form.instance.username = request.user
            new_booking = booking_form.save(commit=False)
            new_booking.date_time = datetime.combine(date_converted, time_converted)
            # --- Confirmation email ---
            # Prefixes
            recipient = [
                "anetasglimmer@gmail.com"
            ]  # Send the email to myself as confirmation
            recipient.append(request.user.email)  # Add email of user creating booking
            subject = "Booking at Aneta's Glimmer"
            from_address = "anetasglimmer@gmail.com"
            date_email = date_converted.strftime("%d.%m.%Y")
            time_email = time_converted.strftime("%H:%M")
            artists_email = Artists.objects.filter(id=request.POST["booked_artist"])
            for artist in artists_email:
                artist_email = artist.name
            message = f"We are sending you this email to let you know that your booking for {date_email} at {time_email} with {artist_email} is pending confirmation. See you then ;)"
            # Send the email
            send_mail(subject, message, from_address, recipient)
            # Save booking into database
            new_booking.save()
        else:
            booking_form = self.form()
        return redirect("my-bookings")
