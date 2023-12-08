from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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

