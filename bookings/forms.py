from django.shortcuts import redirect
from django import forms
from bookings.models import Bookings





class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['date_time']

    your_datetime_field = forms.SplitDateTimeField(
        label='Date and Time',
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        hours=range(9, 16)
    )
