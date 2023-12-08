from django.urls import path
from styles import views


urlpatterns = [
    path("", views.StylesView.as_view(), name="styles"),
    path("<slug:slug>/", views.StyleDetailView.as_view(), name="style-detail"),
]