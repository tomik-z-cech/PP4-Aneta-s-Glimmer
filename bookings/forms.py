from django import forms
from allauth.account.forms import SignupForm
from .models import UserProfile

class GlimmerSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    phone_number = forms.CharField(max_length=15, label='Phone Number', required=True)
    marketing = forms.BooleanField(label='Marketing option', required=False)

    def save(self, request):
        user = super(GlimmerSignupForm, self).save(request)
        user_profile = UserProfile.objects.create(
            user=user, 
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            marketing=self.cleaned_data['marketing'],
            )
        user.userprofile = user_profile
        return user