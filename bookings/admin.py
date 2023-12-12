from django.contrib import admin
from bookings.models import Bookings

# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):

    list_display = ('booked_artist',)
