from django.urls import path
from styles import views


urlpatterns = [
    path("styles/", views.StylesView.as_view(), name="styles"),
    path("styles/<slug:slug>/", views.StyleDetailView.as_view(), name="style-detail"),
]