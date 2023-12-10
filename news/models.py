from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Set variable for published posts
IS_PUBLISHED = ((0, 'Not Published'), (1, 'Published'))
# Set variable for approved comments
IS_APPROVED = ((0, 'Not Approved'), (1, 'Approved'))

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
    approved = models.IntegerField(choices=IS_APPROVED, default=0)

    class Meta:
        ordering = ['created_on']
        verbose_name = 'News Comment'

    def __str__(self):
        return f"Comment {self.comment_body} by {self.username}"
    
