from . import views
from django.urls import path


urlpatterns = [
    path('', views.NewsList.as_view(), name='home'),
    path('news/<slug:slug>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('styles/', views.StylesView.as_view(), name='styles'),
    path('styles/<slug:slug>/', views.StyleDetailView.as_view(), name='style-detail'),
    path('artists/', views.TeamView.as_view(), name='artists'),
    path('artists/<slug:slug>/', views.TeamDetailView.as_view(), name='artist-detail'),
    ]