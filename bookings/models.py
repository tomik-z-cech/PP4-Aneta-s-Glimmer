from django.db import models
from django.contrib.auth.models import User
from artists.models import Artists
from styles.models import StylesAvailable


# Booking
class Bookings(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='booking')
    date_time = models.DateTimeField()
    booked_artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='booking')
    booked_style = models.ForeignKey(StylesAvailable, on_delete=models.CASCADE, related_name='booking')
    booking_confirmed = models.BooleanField(default=False)
    booking_done = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Booking'

    def __str__(self):
        return f"User {self.username}"
