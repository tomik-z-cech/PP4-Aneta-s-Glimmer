from django.contrib import admin
from django.core.mail import send_mail
from bookings.models import Bookings
from artists.models import Artists
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = (
        "booking_date",
        "booking_time",
        "username",
        "booked_artist",
        "booked_style",
        "booking_status",
    )
    # ordering = ("-date",)
    actions = ["confirm_bookings", "done_bookings"]
    list_filter = ("booking_status", "booked_artist")
    readonly_fields = ("rating",)

    def confirm_bookings(self, request, queryset):
        # Prefixes for confirmation email
        subject = "Confirmed Booking at Aneta's Glimmer"  # Subject
        from_address = "anetasglimmer@gmail.com"  # From
        for booking in queryset:
            if (
                booking.booking_status == 0
            ):  # Status can be changed only for pending bookings
                recipient = [
                    "anetasglimmer@gmail.com"
                ]  # Send the email to myself as confirmation
                user_in_booking = User.objects.get(username=booking.username)
                recipient.append(
                    user_in_booking.email
                )  # Add email of user that their booking was confirmed
                date_email = booking.date_time.strftime(
                    "%d.%m.%Y"
                )  # Stringify date for email
                time_email = booking.date_time.strftime(
                    "%H:%M"
                )  # Stringify time for email
                message = f"We are sending you this email to confirm that your booking for {date_email} at {time_email} with {booking.booked_artist} is now confirmed. See you then ;) "
                send_mail(subject, message, from_address, recipient)  # Send the email
                booking.booking_status = 1  # Change status
                booking.save()  # Save

    def done_bookings(self, request, queryset):
        # Prefixes for confirmation email
        subject = "Thank you for your visit at Aneta's Glimmer"  # Subject
        from_address = "anetasglimmer@gmail.com"  # From
        for booking in queryset:
            if (
                booking.booking_status == 1
            ):  # Status can be changed only for confirmed bookings
                recipient = [
                    "anetasglimmer@gmail.com"
                ]  # Send the email to myself as confirmation
                user_in_booking = User.objects.get(username=booking.username)
                recipient.append(
                    user_in_booking.email
                )  # Add email of user that their booking was done
                date_email = booking.date_time.strftime(
                    "%d.%m.%Y"
                )  # Stringify date for email
                time_email = booking.date_time.strftime(
                    "%H:%M"
                )  # Stringify time for email
                message = f"{booking.booked_artist} was very pleased to look after you on {date_email} at {time_email}. Please leave a review ;) "
                send_mail(subject, message, from_address, recipient)  # Send the email
                booking.booking_status = 2  # Change status
                booking.save()  # Save

    def booking_date(self, obj):  # Separate date from date_time
        return obj.date_time.strftime("%d.%m.%Y")  # Return date

    def booking_time(self, obj):
        return obj.date_time.strftime("%H:%M")

    def get_ordering(self, request):
        # Sort by date first, then time
        return ["-date_time", "-date_time__time"]

    booking_date.admin_order_field = "date_time"
    booking_time.admin_order_field = "date_time"

    booking_date.short_description = "Date"
    booking_time.short_description = "Time"

    confirm_bookings.short_description = 'Mark as "CONFIRMED"'
    done_bookings.short_description = 'Mark as "DONE"'
