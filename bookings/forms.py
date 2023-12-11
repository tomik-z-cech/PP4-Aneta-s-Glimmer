from django import forms
from django.utils import timezone
from datetime import datetime, timedelta
from bookings.models import Bookings

class CreateBookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = (
            "date",
            "time",
            "booked_artist",
            "booked_style"
        )

    date = forms.DateField(
        label="Date",
        widget=forms.TextInput(attrs={"type": "date"}),
        help_text="* Please select date of your visit",
    )

    time = forms.ChoiceField(
        label="Time",
        choices=[(f"{h:02d}:00", f"{h:02d}:00") for h in range(9, 17, 1)],
        widget=forms.Select,
        help_text="* Please select time of your visit",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_extra_days = 2
        min_date = timezone.now() + timedelta(days=min_extra_days)
        self.fields['date'].widget.attrs.update({'min': min_date.date()})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Combine date and time to create date_time
        if date and time:
            date_time = datetime.combine(date, time)
            cleaned_data["date_time"] = timezone.make_aware(date_time)

        return cleaned_data
    
