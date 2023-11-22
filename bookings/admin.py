from django.contrib import admin
from .models import NewsPosts, UserProfile, NewsComments, StylesAvailable, Artists, Bookings, StylesComments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('full_name',)
    
@admin.register(NewsPosts)
class NewsPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_body')
    
@admin.register(NewsComments)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('username', 'comment_body', 'post', 'approved')

@admin.register(StylesComments)
class StylesCommentAdmin(admin.ModelAdmin):

    list_display = ('username', 'comment_body', 'style', 'approved')    

@admin.register(StylesAvailable)
class StylesAvailableAdmin(admin.ModelAdmin):

    list_display = ('style_name',)
    prepopulated_fields = {'slug': ('style_name',)}
    
@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):

    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):

    list_display = ('booked_artist',)
