from django.contrib import admin
from artists.models import Artists


# Register your models here.
@admin.register(Artists)
class ArtistsAdmin(admin.ModelAdmin):
    """
    Register Artists Admin
    """

    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}
