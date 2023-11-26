from django.contrib import admin
from .models import NewsPosts, UserProfile, NewsComments, StylesAvailable, Artists, Bookings, StylesComments
from django.contrib.auth.models import User
from django_summernote.admin import SummernoteModelAdmin

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class ProfileAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'marketing')

    def first_name(self, obj):
        return obj.userprofile.first_name if hasattr(obj, 'userprofile') else ''

    def last_name(self, obj):
        return obj.userprofile.last_name if hasattr(obj, 'userprofile') else ''
    
    def phone_number(self, obj):
        return obj.userprofile.phone_number if hasattr(obj, 'userprofile') else ''
    
    def marketing(self, obj):
        return obj.userprofile.marketing if hasattr(obj, 'userprofile') else ''

admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)    


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
