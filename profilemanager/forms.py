from django import forms
from allauth.account.forms import SignupForm
from profilemanager.models import UserProfile


class GlimmerSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name", required=True, widget=forms.TextInput(attrs={'placeholder': 'Your first name'}),)
    last_name = forms.CharField(max_length=30, label="Last Name", required=True, widget=forms.TextInput(attrs={'placeholder': 'Your last name'}),)
    phone_number = forms.CharField(max_length=15, label="Phone Number", required=True, widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}),)
    marketing = forms.BooleanField(
        label="Would you like to receive marketing materials ?",
        required=False,
        initial=True,
    )
    t_and_c = forms.BooleanField(
        label="Agree to terms and conditions ?", required=True, initial=False
    )

    def save(self, request):
        user = super(GlimmerSignupForm, self).save(request)
        user_profile = UserProfile.objects.create(
            user=user,
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            phone_number=self.cleaned_data["phone_number"],
            marketing=self.cleaned_data["marketing"],
        )
        user.userprofile = user_profile
        return user


class UpdateDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["first_name", "last_name", "phone_number", "marketing"]
