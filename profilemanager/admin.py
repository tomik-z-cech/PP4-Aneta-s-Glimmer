from django.contrib import admin
from django.contrib.auth.models import User
from profilemanager.models import UserProfile

# Register your models here.
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class ProfileAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline, )
    list_display = ('last_name', 'first_name', 'email', 'username', 'phone_number', 'marketing', 'email')

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
 