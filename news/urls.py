from django.urls import path
from news import views

urlpatterns = [
    path("news", views.AllNewsView.as_view(), name="all-news"),
    path("news/<slug:slug>/", views.NewsDetailView.as_view(), name="news-detail"),
    path("like/<slug:slug>", views.NewsPostLike.as_view(), name="news-like"),
]