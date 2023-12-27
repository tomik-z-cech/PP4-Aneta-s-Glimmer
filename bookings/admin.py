# PEP8
# Imports
from django.contrib import admin
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from bookings.models import Bookings


# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    """
    Registers bookings to admin
    """
    list_display = (
        "booking_date",
        "booking_time",
        "username",
        "booked_artist",
        "booked_style",
        "booking_status",
    )
    # Quick actions
    actions = ["confirm_bookings", "done_bookings"]
    # Lists
    list_filter = ("booking_status", "booked_artist")
    # Firld that can't be changed by admin
    readonly_fields = ("rating",)

    def confirm_bookings(self, request, queryset):
        """
        Method changes status
        of pending bookings to confirmed
        """
        for booking in queryset:
            if (
                booking.booking_status == 0
            ):  # Status can be changed only for pending bookings
                user_in_booking = User.objects.get(username=booking.username)
                booking.booking_status = 1  # Change status
                booking.save()  # Save
                # Prefixes for confirmation email
                recipient = [
                    "anetasglimmer@gmail.com"
                ]  # Send the email to myself as confirmation
                recipient.append(
                    user_in_booking.email
                )  # Add email of user creating booking
                subject = "Confirmed Booking at Aneta's Glimmer"  # Subject
                from_address = "anetasglimmer@gmail.com"  # From
                date_email = booking.date_time.strftime(
                    "%d.%m.%Y"
                )  # Stringify date for email
                time_email = booking.date_time.strftime(
                    "%H:%M"
                )  # Stringify time for email
                html_message = render_to_string(
                    "emails/confirmed_booking_mail.html",
                    {
                        "user": User.objects.get(username=booking.username),
                        "date": date_email,
                        "time": time_email,
                        "artist": booking.booked_artist,
                        "ref_number": booking.pk,
                    },
                )
                message = strip_tags(html_message)
                send_mail(
                    subject,
                    message,
                    from_address,
                    recipient,
                    html_message=html_message
                )

    def done_bookings(self, request, queryset):
        """
        Method changes status
        of confirmed bookings to done
        """
        for booking in queryset:
            if (
                booking.booking_status == 1
            ):  # Status can be changed only for confirmed bookings
                user_in_booking = User.objects.get(username=booking.username)
                booking.booking_status = 2  # Change status
                booking.save()  # Save
                # Prefixes for confirmation email
                recipient = [
                    "anetasglimmer@gmail.com"
                ]  # Send the email to myself as confirmation
                recipient.append(
                    user_in_booking.email
                )  # Add email of user creating booking
                # Subject
                subject = "Thank you for your visit at Aneta's Glimmer"
                from_address = "anetasglimmer@gmail.com"  # From
                date_email = booking.date_time.strftime(
                    "%d.%m.%Y"
                )  # Stringify date for email
                time_email = booking.date_time.strftime(
                    "%H:%M"
                )  # Stringify time for email
                html_message = render_to_string(
                    "emails/done_booking_mail.html",
                    {
                        "user": User.objects.get(username=booking.username),
                        "date": date_email,
                        "time": time_email,
                        "artist": booking.booked_artist,
                        "ref_number": booking.pk,
                    },
                )
                message = strip_tags(html_message)
                send_mail(
                    subject,
                    message,
                    from_address,
                    recipient,
                    html_message=html_message
                )

    def booking_date(self, obj):  # Separate date from date_time
        return obj.date_time.strftime("%d.%m.%Y")  # Return date

    def booking_time(self, obj):  # Separate time from date_time
        return obj.date_time.strftime("%H:%M")  # Return time

    def get_ordering(self, request):
        # Sort by date first, then time
        return ["-date_time", "-date_time__time"]

    booking_date.admin_order_field = "date_time"
    booking_time.admin_order_field = "date_time"

    booking_date.short_description = "Date"
    booking_time.short_description = "Time"

    confirm_bookings.short_description = 'Mark as "CONFIRMED"'
    done_bookings.short_description = 'Mark as "DONE"'
