from django.contrib import admin
from bookings.models import Bookings

# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):

    list_display = ('date_time','booked_artist','booked_style','booking_status')
    ordering = ('-date_time',)
