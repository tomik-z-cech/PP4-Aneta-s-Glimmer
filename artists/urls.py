# PEP8
# Imports
from django.urls import path
from artists import views

# Artists URL Patterns
urlpatterns = [
    path("", views.TeamView.as_view(), name="artists"),
    path("<slug:slug>/", views.TeamDetailView.as_view(), name="artist-detail"),
]
