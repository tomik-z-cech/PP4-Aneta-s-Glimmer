from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from styles.models import StylesAvailable

# Artists
class Artists(models.Model):
    name = models.CharField(max_length=100, unique=True)
    profile_picture = CloudinaryField('image', default='default_artist_pp')
    bio = models.TextField()
    public_profile = models.URLField(blank=False, null=False)
    start_date = models.DateField()
    styles = models.ManyToManyField(StylesAvailable, blank=False)
    rating = models.FloatField(default=5.0)
    bookings_total = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Artist'
    
    def __str__(self):
        return self.name
    