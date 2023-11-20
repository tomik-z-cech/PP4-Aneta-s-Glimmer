from django.contrib import admin
from .models import NewsPosts, UserProfile, Comments, StylesAvailable, Artists, Bookings
from django_summernote.admin import SummernoteModelAdmin

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('full_name',)
    
@admin.register(NewsPosts)
class NewsPostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_body')
    
@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'comment_body', 'post', 'approved')
    

@admin.register(StylesAvailable)
class StylesAvailableAdmin(admin.ModelAdmin):

    list_display = ('style_name',)
    
@admin.register(Artists)
class StylesAvailableAdmin(admin.ModelAdmin):

    list_display = ('name',)
    
@admin.register(Bookings)
class StylesAvailableAdmin(admin.ModelAdmin):

    list_display = ('booked_artist',)
