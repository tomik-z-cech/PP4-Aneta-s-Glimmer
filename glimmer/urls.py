# Aneta's Glimmer URL configuration

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("landing.urls")),
    path("news/", include("news.urls")),
    path("styles/", include("styles.urls")),
    path("artists/", include("artists.urls")),
    path("profilemanager/", include("profilemanager.urls")),
]
