from django.urls import path
from . import views


urlpatterns = [
    path("", views.LandingPageView.as_view(), name="home"),
    path("news", views.AllNewsView.as_view(), name="all-news"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news-detail"),
    path("styles/", views.StylesView.as_view(), name="styles"),
    path("styles/<slug:slug>/", views.StyleDetailView.as_view(), name="style-detail"),
    path("artists/", views.TeamView.as_view(), name="artists"),
    path("artists/<slug:slug>/", views.TeamDetailView.as_view(), name="artist-detail"),
    path("details/", views.MyDetailsView.as_view(), name="my-details"),
    path("deleteprofile/", views.DeleteMyProfileView.as_view(), name="delete-profile"),
    path("like/<slug:slug>", views.NewsPostLike.as_view(), name="news-like"),
]
