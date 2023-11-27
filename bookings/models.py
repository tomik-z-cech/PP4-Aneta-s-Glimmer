from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Set variable for published posts
IS_PUBLISHED = ((0, 'Not Published'), (1, 'Published'))

# User Profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    marketing = models.BooleanField()
    
    class Meta:
        verbose_name = 'User Profile'
    
    def __str__(self):
        return self.first_name
    

# Styles Available
class StylesAvailable(models.Model):
    style_name = models.CharField(max_length=100)
    style_description = models.TextField()
    sample_image = CloudinaryField('image', default='default_sample_image')
    likes = models.ManyToManyField(User, related_name='style_likes', blank=True)
    want_to_try = models.ManyToManyField(User, related_name='want_to_try', blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Available Style'
    
    def __str__(self):
        return self.style_name
    
    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_tries(self):
        return self.want_to_try.count()
    

# Style Comments
class StylesComments(models.Model):

    style = models.ForeignKey(StylesAvailable, on_delete=models.CASCADE, related_name='style_comments')
    username = models.CharField(max_length=80)
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'Style Comment'

    def __str__(self):
        return f"Comment {self.comment_body} by {self.username}"

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
    
# News
class NewsPosts(models.Model):
    title = models.CharField(max_length=200, unique=True)
    heading_image = CloudinaryField('image', default='default_heading_image')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news')
    post_body = models.TextField(blank=False, null=False, default='text')
    created_on = models.DateTimeField(auto_now_add=True)
    is_published = models.IntegerField(choices=IS_PUBLISHED, default=0)
    likes = models.ManyToManyField(User, related_name='news_likes', blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ['-created_on']
        verbose_name = 'News Post'

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
# News Comments
class NewsComments(models.Model):

    post = models.ForeignKey(NewsPosts, on_delete=models.CASCADE, related_name='news_comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_comments')
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'News Comment'

    def __str__(self):
        return f"Comment {self.comment_body} by {self.username}"
    