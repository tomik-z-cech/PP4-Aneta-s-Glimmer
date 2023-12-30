# PEP8
# Imports
from django.urls import path
from administrator import views

urlpatterns = [
    path("", views.AllAdminView.as_view(), name="all-admin"),
]
