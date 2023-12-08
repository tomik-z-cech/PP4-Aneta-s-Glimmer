from django.urls import path
from artists import views


urlpatterns = [
    path("artists/", views.TeamView.as_view(), name="artists"),
    path("artists/<slug:slug>/", views.TeamDetailView.as_view(), name="artist-detail"),
]