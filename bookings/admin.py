from django.contrib import admin
from django.core.mail import send_mail
from bookings.models import Bookings
from django.contrib.auth.models import User


# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ("date_time", "booked_artist", "booked_style", "booking_status")
    ordering = ("-date_time",)
    actions = ["confirm_bookings"]

    def confirm_bookings(self, request, queryset):
        # Prefixes for confirmation email
        subject = "Confirmed Booking at Aneta's Glimmer"  # Subject
        from_address = "anetasglimmer@gmail.com"  # From
        for booking in queryset:
            if (
                booking.booking_status == 0
            ):  # Status can be changed only for pending bookings
                recipient = ["anetasglimmer@gmail.com"]  # Send the email to myself as confirmation
                user_in_booking = User.objects.get(username=booking.username)
                recipient.append(user_in_booking.email)  # Add email of user that their booking was confirmed
                date_email = booking.date_time.strftime(
                    "%d.%m.%Y"
                )  # Stringify date for email
                time_email = booking.date_time.strftime(
                    "%H:%M"
                )  # Stringify time for email
                message = f"We are sending you this email to confirm that your booking for {date_email} at {time_email} with {booking.booked_artist} is now confirmed. See you then ;) "
                send_mail(subject, message, from_address, recipient)  # Send the email
                booking.booking_status = 1 # Change status
                booking.save() # Save
                
    
    confirm_bookings.short_description = 'Mark as "CONFIRMED"'
    done_bookings.short_description = 'Mark as "DONE"'
