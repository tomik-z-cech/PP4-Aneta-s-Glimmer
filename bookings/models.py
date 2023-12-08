from django.db import models
from artists.models import Artists
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Booking
class Bookings(models.Model):
    date = models.DateTimeField()
    time = models.DateTimeField()
    booked_artist = models.ForeignKey(Artists, on_delete=models.CASCADE, related_name='booking')
    booking_confirmed = models.BooleanField(default=False) 
    booking_done = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Booking'
    
    def __str__(self):
        return f"{self.date.strftime('%d-%m-%Y %H:%M')} - {self.booked_artist.name}"