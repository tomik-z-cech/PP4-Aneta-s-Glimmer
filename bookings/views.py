# Imports
from datetime import datetime
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import generic
from bookings.models import Bookings
from bookings.forms import BookingForm
from artists.models import Artists

class BookingOptionsView(generic.ListView):
    def booking_options(request):
        """
        Function returns data to the template based on user selection
        """
        # booked_style_new = request.session.get("booked_style_new", None)
        # Create pseudo variables for booking
        booked_artist_new = request.session.get("booked_artist_new", None)
        received_value = request.GET.get("selected_value", None)
        field_name = request.GET.get("field_name", None)
        # If request comes from field #id_booked_style
        if field_name == "#id_booked_style":
            request.session[
                "booked_style_new"
            ] = received_value  # Save received value "booked style"
            options = [
                '<option value="0" selected>Select Artist</option>'
            ]  # Heading option for Select artist field
            artists_with_style = Artists.objects.filter(
                styles__in=[received_value]
            )  # Queryset for artists with the selected style
            for artist in artists_with_style:  # For each artist
                artist_id = str(artist.id)  # Stringify id field
                options.append(
                    '<option value="' + artist_id + '">' + artist.name + "</option>"
                )  # Create a list of artists with the selected style
            data = {"options": options}  # Data to send back
        # If request comes from field #id_booked_artist
        elif field_name == "#id_booked_artist":
            request.session[
                "booked_artist_new"
            ] = received_value  # Save received value "booked style"
            data = {}  # No data to send back
        # If request comes from field #id_date
        elif field_name == "#id_date":
            options = [
                '<option value="0">Select Time</option>'
            ]  # Heading option for Select time field
            booked_date_new = received_value  # Save received value "booked date"
            bookings_artist = Bookings.objects.filter(
                booked_artist__in=[booked_artist_new]
            )  # Queryset for bookings of selected artist
            bookings_artist_day = bookings_artist.filter(
                date_time__date=booked_date_new
            )  # Queryset for bookings of selected artist filter by date
            time_range = [
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00",
            ]  # Select time options
            # Loops selection for times and filtered bookings not available
            for i in time_range:
                match = 0
                for booking in bookings_artist_day:
                    if i == booking.date_time.time().strftime("%H:%M"):
                        match = 1
                # If time not yet booked - enable option
                if match == 0:
                    options.append('<option value="' + i + ':00">' + i + "</option>")
                # If time already booked - disable option
                else:
                    options.append(
                        '<option value="' + i + ':00" disabled>' + i + "</option>"
                    )
            data = {"options": options}  # Data to send back
        return JsonResponse(data)  # Return with JSON response


class MyBookingsView(generic.ListView):
    """
    Class for viewing all bookings for logged in user
    """

    template_name = "bookings/bookings.html"  # Template
    model = Bookings

    def get(self, request, *args, **kwargs):
        """Method GET filters all bookings by user"""
        login_user = request.user  # Request logged in user
        user_bookings = Bookings.objects.filter(username=login_user)  # Filter bookings
        return render(  # Render template
            request,
            self.template_name,
            {
                "bookings": user_bookings,
            },
        )
    
    def cancel_request(request, request_booking_pk):
        requested_booking = Bookings.objects.get(pk=request_booking_pk)  # Get booking
        return render(  # Render template
            request,
            "bookings/booking_cancel_confirm.html",
            {
                "booking_to_cancel": requested_booking
            },
        )


class NewBookingView(generic.ListView):
    """
    Class for creating new bookings
    """

    template_name = "bookings/new_booking.html"  # Template
    form = BookingForm  # New bookings form
    success_url = "/bookings/"  # URL to redirect after successful booking

    def get(self, request, *args, **kwargs):
        """
        Function generates booking form into template
        """
        return render(
            request,
            self.template_name,
            {
                "new_booking_form": BookingForm(),  # Booking form
            },
        )

    def post(self, request, *args, **kwargs):
        """
        Function triggers when submit button on booking form is pressed
        """
        booking_form = self.form(data=request.POST)
        if booking_form.is_valid():
            date_converted = datetime.strptime(
                request.POST["date"], "%Y-%m-%d"
            ).date()  # Convert str date to datetime date
            time_converted = datetime.strptime(
                request.POST["time"], "%H:%M:%S"
            ).time()  # Conver str time to datetime time
            booking_form.instance.username = request.user  # Request username
            new_booking = booking_form.save(commit=False)
            new_booking.date_time = datetime.combine(
                date_converted, time_converted
            )  # Combine date and time
            # Prefixes for confirmation email
            recipient = [
                "anetasglimmer@gmail.com"
            ]  # Send the email to myself as confirmation
            recipient.append(request.user.email)  # Add email of user creating booking
            subject = "New Booking at Aneta's Glimmer"  # Subject
            from_address = "anetasglimmer@gmail.com"  # From
            date_email = date_converted.strftime("%d.%m.%Y")  # Stringify date for email
            time_email = time_converted.strftime("%H:%M")  # Stringify time for email
            select_artist = Artists.objects.get(
                id=request.POST["booked_artist"]
            )  # Queryset to select artist by id
            artist_email = select_artist.name  # Save artist's name for email
            message = f"We are sending you this email to let you know that your booking for {date_email} at {time_email} with {artist_email} is pending confirmation. We will confirm that shortly ;)"
            send_mail(subject, message, from_address, recipient)  # Send the email
            new_booking.save()  # Save booking into database
        else:
            booking_form = self.form()
        return redirect("my-bookings")  # Redirect back to my-bookings
    

class EditBookingView(generic.ListView):
    """
    Class for creating new bookings
    """

    template_name = "bookings/edit_booking.html"  # Template
    form = BookingForm  # New bookings form
    success_url = "/bookings/"  # URL to redirect after successful booking

    def get(self, request, edit_booking_pk, *args, **kwargs):
        """
        Function generates booking form into template
        """
        booking_instance = Bookings.objects.get(pk=edit_booking_pk)
        edit_booking_form = BookingForm(instance=booking_instance)
        print(edit_booking_pk)
        print(edit_booking_form)
        return render(
            request,
            self.template_name,
            {
                "edit_booking_form": edit_booking_form,  # Booking form
            },
        )


    def post(self, request, *args, **kwargs):
        """
        Function triggers when submit button on booking form is pressed
        """
        booking_form = self.form(data=request.POST)
        if booking_form.is_valid():
            date_converted = datetime.strptime(
                request.POST["date"], "%Y-%m-%d"
            ).date()  # Convert str date to datetime date
            time_converted = datetime.strptime(
                request.POST["time"], "%H:%M:%S"
            ).time()  # Conver str time to datetime time
            booking_form.instance.username = request.user  # Request username
            new_booking = booking_form.save(commit=False)
            new_booking.date_time = datetime.combine(
                date_converted, time_converted
            )  # Combine date and time
            # Prefixes for confirmation email
            recipient = [
                "anetasglimmer@gmail.com"
            ]  # Send the email to myself as confirmation
            recipient.append(request.user.email)  # Add email of user creating booking
            subject = "New Booking at Aneta's Glimmer"  # Subject
            from_address = "anetasglimmer@gmail.com"  # From
            date_email = date_converted.strftime("%d.%m.%Y")  # Stringify date for email
            time_email = time_converted.strftime("%H:%M")  # Stringify time for email
            select_artist = Artists.objects.get(
                id=request.POST["booked_artist"]
            )  # Queryset to select artist by id
            artist_email = select_artist.name  # Save artist's name for email
            message = f"We are sending you this email to let you know that your booking for {date_email} at {time_email} with {artist_email} is pending confirmation. We will confirm that shortly ;)"
            # send_mail(subject, message, from_address, recipient)  # Send the email
            # new_booking.save()  # Save booking into database
        else:
            booking_form = self.form()
        return redirect("my-bookings")  # Redirect back to my-bookings

class CancelBookingView(generic.ListView):
    def get(self, request, cancel_booking_pk, *args, **kwargs):
        booking_to_cancel = Bookings.objects.get(pk=cancel_booking_pk) # Queryset for booking to cancel
        # Prefixes for confirmation email
        recipient = [
            "anetasglimmer@gmail.com"
        ]  # Send the email to myself as confirmation
        recipient.append(request.user.email)  # Add email of user cancelling booking
        subject = "Cancelled Booking at Aneta's Glimmer"  # Subject
        from_address = "anetasglimmer@gmail.com"  # From
        date_email = booking_to_cancel.date_time.strftime("%d.%m.%Y")  # Stringify date for email
        time_email = booking_to_cancel.date_time.strftime("%H:%M")  # Stringify time for email
        message = f"We are sending you this email to confirm that your booking for {date_email} at {time_email} with {booking_to_cancel.booked_artist} was cancelled. We are sorry to see that :( "
        send_mail(subject, message, from_address, recipient)  # Send the email
        booking_to_cancel.delete() # Delete booking from DB
        return redirect("my-bookings") # Return to my bookings

class RateBookingView(generic.ListView):
    def get(self, request, rate_booking_pk, score, *args, **kwargs):
        print(rate_booking_pk, score)
        booking_to_rate = Bookings.objects.get(pk=rate_booking_pk)
        booking_to_rate.is_rated = 1 # Change status
        booking_to_rate.rating = score # Add rating
        booking_to_rate.save() # Save
        return redirect("my-bookings") # Return to my bookings
        