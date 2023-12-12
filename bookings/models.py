from django.db import models
from django.contrib.auth.models import User
from artists.models import Artists
from styles.models import StylesAvailable

BOOKING_STATUS = ((0, 'Pending'), (1, 'Confirmed'), (2, 'Done'))


# Booking
class Bookings(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    date_time = models.DateTimeField(null=True)
    booked_artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='booking')
    booked_style = models.ForeignKey(StylesAvailable, on_delete=models.CASCADE, related_name='booking')
    booking_status = models.IntegerField(choices=BOOKING_STATUS, default=0)

    class Meta:
        verbose_name = 'Booking'

    def __str__(self):
        return f"User {self.username}"
