from django.contrib import admin
from news.models import NewsPosts, NewsComments
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(NewsPosts)
class NewsPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_body')
    
@admin.register(NewsComments)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('username', 'comment_body', 'post', 'approved')

