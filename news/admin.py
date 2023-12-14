# Imports
from django.contrib import admin
from news.models import NewsPosts, NewsComments
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(NewsPosts)
class NewsPostAdmin(SummernoteModelAdmin):
    """Class regsiters News Posts to Admin"""

    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = "post_body"


@admin.register(NewsComments)
class CommentAdmin(admin.ModelAdmin):
    """Class resgisters News Comments to Admin"""

    list_display = ("username", "comment_body", "post", "approved")
