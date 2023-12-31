# PEP8
# Imports
from django.urls import path
from landing import views


urlpatterns = [
    path("", views.LandingPageView.as_view(), name="home"),
    path("search/", views.LandingPageView.search, name="search"),
]
