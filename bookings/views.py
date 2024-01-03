# PEP8
# Imports
from django.contrib import messages
from django.core.exceptions import PermissionDenied  # Throws 403
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)  # Views security
# Methods security
from django.contrib.auth.decorators import login_required
# Time format with timezone stamp + strip tags
from django.utils import timezone
from django.utils.html import strip_tags
from datetime import datetime, timedelta  # Time functions
from django.core.mail import send_mail  # Email
from django.template.loader import render_to_string
from django.http import JsonResponse, Http404  # Responses
from django.shortcuts import render, redirect, get_object_or_404  # Responses
from django.views import generic
from bookings.models import Bookings
from bookings.forms import BookingForm
from artists.models import Artists


class BookingOptionsView(generic.ListView):
    @login_required
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
                    '<option value="'+artist_id+'">'+artist.name+"</option>"
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
            # Save received value "booked date"
            booked_date_new = received_value
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
                    options.append(
                        '<option value="' + i + ':00">' + i + "</option>"
                        )
                # If time already booked - disable option
                else:
                    options.append(
                        '<option value="'+i+':00" disabled>' + i + "</option>"
                    )
            data = {"options": options}  # Data to send back
        return JsonResponse(data)  # Return with JSON response


class MyBookingsView(LoginRequiredMixin, generic.ListView):
    """
    Class for viewing all bookings for logged in user
    """

    template_name = "bookings/bookings.html"  # Template
    model = Bookings

    def get(self, request, *args, **kwargs):
        """Method GET filters all bookings by user"""
        login_user = request.user  # Request logged in user
        if login_user.is_superuser:
            print("Superuser")
            return redirect("all-admin")
        else:
            pending_bookings = (
                Bookings.objects.filter(username=login_user)
                .filter(booking_status=0)
                .order_by("-date_time")
            )  # Filter pending bookings
            confirmed_bookings = (
                Bookings.objects.filter(username=login_user)
                .filter(booking_status=1)
                .order_by("-date_time")
            )
            done_bookings = (
                Bookings.objects.filter(username=login_user)
                .filter(booking_status=2)
                .order_by("-date_time")
            )
            last_minutes = []
            all_artists = Artists.objects.all()
            today = timezone.now().date()
            tommorrow = timezone.now().date() + timedelta(days=1)
            for artist in all_artists:
                # ---
                bookings_tommorrow = Bookings.objects.filter(
                    booked_artist=artist, date_time__date=tommorrow
                ).count()
                free_tommorrow = 8 - bookings_tommorrow
                bookings_today_after_now = Bookings.objects.filter(
                    booked_artist=artist,
                    date_time__date=today,
                    date_time__gt=timezone.now(),
                ).count()
                time_now = timezone.now().time()
                if (
                    time_now >= datetime.strptime("00:00", "%H:%M").time()
                    and time_now < datetime.strptime("09:00", "%H:%M").time()
                ):
                    slots_left_today = 8
                elif (
                    time_now >= datetime.strptime("09:00", "%H:%M").time()
                    and time_now < datetime.strptime("10:00", "%H:%M").time()
                ):
                    slots_left_today = 7
                elif (
                    time_now >= datetime.strptime("10:00", "%H:%M").time()
                    and time_now < datetime.strptime("11:00", "%H:%M").time()
                ):
                    slots_left_today = 6
                elif (
                    time_now >= datetime.strptime("11:00", "%H:%M").time()
                    and time_now < datetime.strptime("12:00", "%H:%M").time()
                ):
                    slots_left_today = 5
                elif (
                    time_now >= datetime.strptime("12:00", "%H:%M").time()
                    and time_now < datetime.strptime("13:00", "%H:%M").time()
                ):
                    slots_left_today = 4
                elif (
                    time_now >= datetime.strptime("13:00", "%H:%M").time()
                    and time_now < datetime.strptime("14:00", "%H:%M").time()
                ):
                    slots_left_today = 3
                elif (
                    time_now >= datetime.strptime("14:00", "%H:%M").time()
                    and time_now < datetime.strptime("15:00", "%H:%M").time()
                ):
                    slots_left_today = 2
                elif (
                    time_now >= datetime.strptime("15:00", "%H:%M").time()
                    and time_now < datetime.strptime("16:00", "%H:%M").time()
                ):
                    slots_left_today = 1
                else:
                    slots_left_today = 0
                free_today = slots_left_today - bookings_today_after_now
                last_minutes.append(
                    {
                        "name": artist.name,
                        "slug": artist.slug,
                        "free_today": free_today,
                        "free_tomorrow": free_tommorrow,
                    }
                )
            # ---
            return render(  # Render template
                request,
                self.template_name,
                {
                    "pending_bookings": pending_bookings,
                    "confirmed_bookings": confirmed_bookings,
                    "done_bookings": done_bookings,
                    "last_minutes": last_minutes,
                },
            )

    @login_required
    def cancel_request(self, request, request_booking_pk):
        """This method redirects user to confirm page"""
        requested_booking = get_object_or_404(
            Bookings, pk=request_booking_pk
        )  # Get booking
        if request.user == requested_booking.username:
            return render(  # Render template
                request,
                "bookings/booking_cancel_confirm.html",
                {"booking_to_cancel": requested_booking},
            )
        else:
            raise PermissionDenied("You do not have permission access !")


class NewBookingView(LoginRequiredMixin, generic.ListView):
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
            ).time()  # Convert str time to datetime time
            booking_form.instance.username = request.user  # Request username
            new_booking = booking_form.save(commit=False)
            new_booking.date_time = datetime.combine(
                date_converted, time_converted
            )  # Combine date and time
            new_booking.date_time = timezone.make_aware(new_booking.date_time)
            new_booking.save()  # Save booking into database
            messages.add_message(
                request,
                messages.SUCCESS,
                f"You have successfully created booking ref {new_booking.pk}.",
            )  # User message
            # Prefixes for confirmation email
            recipient = [
                "anetasglimmer@gmail.com"
            ]  # Send the email to myself as confirmation
            # Add email of user creating booking
            recipient.append(request.user.email)
            subject = "New Booking at Aneta's Glimmer"  # Subject
            from_address = "anetasglimmer@gmail.com"  # From
            # Stringify date for email
            date_email = date_converted.strftime("%d.%m.%Y")
            # Stringify time for email
            time_email = time_converted.strftime("%H:%M")
            select_artist = Artists.objects.get(
                id=request.POST["booked_artist"]
            )  # Queryset to select artist by id
            artist_email = select_artist.name  # Save artist's name for email
            html_message = render_to_string(
                "emails/new_booking_mail.html",
                {
                    "user": request.user.username,
                    "date": date_email,
                    "time": time_email,
                    "artist": artist_email,
                    "ref_number": new_booking.pk,
                },
            )
            message = strip_tags(html_message)
            from_address = "anetasglimmer@gmail.com"  # From
            send_mail(
                subject,
                message,
                from_address,
                recipient,
                html_message=html_message
            )
        else:
            booking_form = self.form()
        return redirect("my-bookings")  # Redirect back to my-bookings


class EditBookingView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """
    Class for creating new bookings
    """

    template_name = "bookings/edit_booking.html"  # Template
    form = BookingForm  # New bookings form
    success_url = "/bookings/"  # URL to redirect after successful booking

    def test_func(self):
        """Test function to ensure user is the booking creator"""
        booking = get_object_or_404(
            Bookings, pk=self.kwargs["edit_booking_pk"])
        return self.request.user == booking.username

    def get(self, request, edit_booking_pk, *args, **kwargs):
        """
        Function generates booking form into template
        """
        booking_instance = get_object_or_404(Bookings, pk=edit_booking_pk)
        style_edit_form = booking_instance.booked_style
        artist_edit_form = booking_instance.booked_artist
        date_edit_form = booking_instance.date_time.date()
        time_edit_form = booking_instance.date_time.strftime("%H:%M")
        edit_booking_form = BookingForm(
            initial={
                "booked_style": style_edit_form,
                "booked_artist": artist_edit_form,
                "date": date_edit_form,
            }
        )
        return render(
            request,
            self.template_name,
            {
                "edit_booking_form": edit_booking_form,  # Booking form
                "initial_time": time_edit_form,
            },
        )

    def post(self, request, edit_booking_pk, *args, **kwargs):
        """
        Function triggers when submit button on booking form is pressed
        """
        edited_booking = get_object_or_404(Bookings, pk=edit_booking_pk)
        booking_form = self.form(data=request.POST)

        if booking_form.is_valid():
            date_converted = datetime.strptime(
                request.POST["date"], "%Y-%m-%d"
            ).date()  # Convert str date to datetime date
            time_converted = datetime.strptime(
                request.POST["time"], "%H:%M:%S"
            ).time()  # Convert str time to datetime time
            edited_booking.booked_artist = booking_form.cleaned_data[
                "booked_artist"]
            edited_booking.booked_style = booking_form.cleaned_data[
                "booked_style"]
            edited_booking.date_time = datetime.combine(
                date_converted, time_converted)
            edited_booking.date_time = timezone.make_aware(
                edited_booking.date_time)
            edited_booking.booking_status = 0
            edited_booking.save()  # Save booking into database
            messages.add_message(
                request,
                messages.SUCCESS,
                f"You have edited booking ref {edited_booking.pk}.",
            )  # User message
            # Prefixes for confirmation email
            recipient = [
                "anetasglimmer@gmail.com"
            ]  # Send the email to myself as confirmation
            # Add email of user creating booking
            recipient.append(request.user.email)
            subject = "Changed Booking at Aneta's Glimmer"  # Subject
            from_address = "anetasglimmer@gmail.com"  # From
            # Stringify date for email
            date_email = date_converted.strftime("%d.%m.%Y")
            # Stringify time for email
            time_email = time_converted.strftime("%H:%M")
            select_artist = Artists.objects.get(
                id=request.POST["booked_artist"]
            )  # Queryset to select artist by id
            artist_email = select_artist.name  # Save artist's name for email
            html_message = render_to_string(
                "emails/edit_booking_mail.html",
                {
                    "user": request.user.username,
                    "date": date_email,
                    "time": time_email,
                    "artist": artist_email,
                    "ref_number": edited_booking.pk,
                },
            )
            message = strip_tags(html_message)
            from_address = "anetasglimmer@gmail.com"  # From
            send_mail(
                subject,
                message,
                from_address,
                recipient,
                html_message=html_message
            )
        else:
            booking_form = self.form()
        return redirect("my-bookings")  # Redirect back to my-bookings


class CancelBookingView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """
    Class cancels bookings
    """
    def test_func(self):
        """Method test if user is the creator of booking"""
        booking = get_object_or_404(
            Bookings, pk=self.kwargs["cancel_booking_pk"])
        return self.request.user == booking.username

    def get(self, request, cancel_booking_pk, *args, **kwargs):
        """Method GET cancels booking and send confirmation"""
        booking_to_cancel = get_object_or_404(
            Bookings, pk=cancel_booking_pk
        )  # Queryset for booking to cancel
        # Prefixes for confirmation email
        recipient = [
            "anetasglimmer@gmail.com"
        ]  # Send the email to myself as confirmation
        recipient.append(request.user.email)
        # Add email of user creating booking
        subject = "Cancelled Booking at Aneta's Glimmer"  # Subject
        from_address = "anetasglimmer@gmail.com"  # From
        date_email = booking_to_cancel.date_time.strftime(
            "%d.%m.%Y"
        )  # Stringify date for email
        time_email = booking_to_cancel.date_time.strftime(
            "%H:%M"
        )  # Stringify time for email
        html_message = render_to_string(
            "emails/cancel_booking_mail.html",
            {
                "user": request.user.username,
                "date": date_email,
                "time": time_email,
                "artist": booking_to_cancel.booked_artist,
                "ref_number": booking_to_cancel.pk,
            },
        )
        message = strip_tags(html_message)
        from_address = "anetasglimmer@gmail.com"  # From
        send_mail(
            subject,
            message,
            from_address,
            recipient,
            html_message=html_message
            )
        messages.add_message(
            request,
            messages.SUCCESS,
            f"You have canceled booking ref {booking_to_cancel.pk}.",
        )  # User message
        booking_to_cancel.delete()  # Delete booking from DB
        return redirect("my-bookings")  # Return to my bookings


class RateBookingView(
        LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    """
    This class view enables user to rate bookings
    """
    def test_func(self):
        """Method tests if user is the creator of booking"""
        booking = get_object_or_404(
            Bookings, pk=self.kwargs["rate_booking_pk"])
        return self.request.user == booking.username

    def get(self, request, rate_booking_pk, score, *args, **kwargs):
        """Method GET adds score to booking"""
        booking_to_rate = get_object_or_404(Bookings, pk=rate_booking_pk)
        if booking_to_rate.is_rated != 1:
            booking_to_rate.is_rated = 1  # Change status
            booking_to_rate.rating = score  # Add rating
            messages.add_message(
                request,
                messages.SUCCESS,
                f"You have rated booking ref {booking_to_rate.pk}.",
            )  # User message
            booking_to_rate.save()  # Save
            return redirect("my-bookings")  # Return to my bookings
        else:
            raise Http404("Already rated !")
