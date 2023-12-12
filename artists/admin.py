from django.contrib import admin
from artists.models import Artists

# Register your models here.
@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):

    list_display = ('name', 'bookings_total', 'rating')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('-rating',)
    