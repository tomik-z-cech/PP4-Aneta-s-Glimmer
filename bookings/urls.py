from . import views
from django.urls import path


urlpatterns = [
    path('', views.NewsList.as_view(), name='home'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news-detail'),
    ]