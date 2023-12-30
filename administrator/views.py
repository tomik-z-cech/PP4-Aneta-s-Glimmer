# PEP8
# Imports
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.
class AllAdminView(
    LoginRequiredMixin, UserPassesTestMixin, generic.DetailView
):
    """
    Class renders view for admin
    """

    template_name = "administrator/admin_menu.html"  # Template

    def test_func(self):
        """Test function - returns true if user == superuser"""
        return (
            self.request.user.is_authenticated
            and self.request.user.is_superuser
        )

    def get(self, request, *args, **kwargs):
        """Method get"""
        return render(request, self.template_name)  # Render template
