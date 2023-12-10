# Aneta's Glimmer URL configuration

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("accounts/", include("allauth.urls")),
    path("", include("landing.urls")),
    path("news/", include("news.urls")),
    path("styles/", include("styles.urls")),
    path("artists/", include("artists.urls")),
    path("profilemanager/", include("profilemanager.urls")),
    path("bookings/", include("bookings.urls")),
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.png'))
]
