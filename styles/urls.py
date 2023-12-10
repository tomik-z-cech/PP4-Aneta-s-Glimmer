from django.urls import path
from styles import views

urlpatterns = [
    path("", views.StylesView.as_view(), name="styles"),
    path("<slug:slug>/", views.StyleDetailView.as_view(), name="style-detail"),
    path("like/<slug:slug>", views.StyleLike.as_view(), name="style-like"),
    path("try/<slug:slug>", views.StyleTry.as_view(), name="style-try"),
]
