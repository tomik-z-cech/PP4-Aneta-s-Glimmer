# PEP8
# Imports
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=False, null=True)
    last_name = models.CharField(max_length=30, blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    marketing = models.BooleanField()
    t_and_c = models.BooleanField(null=True)

    class Meta:
        verbose_name = "User Profile"

    def __str__(self):
        return self.first_name
