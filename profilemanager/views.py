from django.shortcuts import render, redirect
from django.views import generic
from bookings.models import UserProfile, User
from profilemanager.forms import UpdateDetailsForm

# ----------------------- MY PROFILE VIEWS --------------------- #
class MyDetailsView(generic.ListView):
    template_name = 'profilemanager/my_details.html'
    model = UserProfile
    def get(self, request, *args, **kwargs):
        login_user = request.user
        profile_selected = login_user.userprofile
        details_form = UpdateDetailsForm(instance=profile_selected)
        return render(request, self.template_name,{
            'details_form': details_form,
            'username': login_user.username
            })
    def post(self, request, *args, **kwargs):
        updated_profile = request.user.userprofile
        form = UpdateDetailsForm(request.POST, instance=updated_profile)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        
class DeleteMyProfileView(generic.ListView):
    def get(self, request, *args, **kwargs):
        model = User
        logged_in_user = request.user
        logged_in_user.delete()
        return redirect('home')
