# PEP8
# Imports
from django.contrib import admin
from styles.models import StylesAvailable, StylesComments


# Register your models here.
@admin.register(StylesComments)
class StylesCommentAdmin(admin.ModelAdmin):
    list_display = ("creator", "comment_body", "style", "approved")
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    approve_comments.short_description = "Approve selected comments"


@admin.register(StylesAvailable)
class StylesAvailableAdmin(admin.ModelAdmin):
    list_display = ("style_name",)
    prepopulated_fields = {"slug": ("style_name",)}
