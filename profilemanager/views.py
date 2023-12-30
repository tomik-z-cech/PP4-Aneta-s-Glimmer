# PEP8
# Imports
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import generic
from .models import User
from profilemanager.models import UserProfile
from profilemanager.forms import UpdateDetailsForm


class MyDetailsView(generic.ListView):
    """
    Class generates view for user profile details
    """
    template_name = "profilemanager/my_details.html"
    model = UserProfile

    def get(self, request, *args, **kwargs):
        """Method generates view for profile manager"""
        # Request logged in user
        login_user = request.user
        profile_selected = login_user.userprofile
        # Prepopulate form
        details_form = UpdateDetailsForm(instance=profile_selected)
        # Render template
        return render(
            request,
            self.template_name,
            {"details_form": details_form, "username": login_user.username},
        )

    def post(self, request, *args, **kwargs):
        """Method saves updated user details"""
        updated_profile = request.user.userprofile
        # Updated details from form
        form = UpdateDetailsForm(request.POST, instance=updated_profile)
        # If valid
        if form.is_valid():
            # User message
            messages.add_message(
                request, messages.SUCCESS, f"Your details were updated"
            )
            # Save details
            form.save()
            # Redirect home
            return redirect("home")


class DeleteMyProfileView(generic.ListView):
    """
    Class deletes user profile
    """
    def get(self, request, *args, **kwargs):
        """Method entirely deletes user profile"""
        model = User
        logged_in_user = request.user
        # Delete user profile
        logged_in_user.delete()
        # User message
        messages.add_message(
                request, messages.SUCCESS, f"Your details were updated"
            )
        # Redirect home
        return redirect("home")
