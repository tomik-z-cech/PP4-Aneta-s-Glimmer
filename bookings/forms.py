from django import forms
from django.utils import timezone
from datetime import datetime, timedelta
from bookings.models import Bookings
from styles.models import StylesAvailable


class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = (
            "booked_style",
            "booked_artist",
            "date",
            "time",
        )

    booked_style = forms.ModelChoiceField(queryset=StylesAvailable.objects.all())

    date = forms.DateField(
        label="Date",
        widget=forms.TextInput(attrs={"type": "date"}),
    )

    time = forms.TimeField(
        label="Time",
        widget=forms.Select,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        min_extra_days = 2
        min_date = timezone.now() + timedelta(days=min_extra_days)
        self.fields["date"].widget.attrs.update({"min": min_date.date()})
        style_choices = StylesAvailable.objects.values_list("id", "style_name")
        default_choice = [("0", "Select Style")]
        self.fields["booked_style"].choices = default_choice + list(style_choices)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get("date")
        time = cleaned_data.get("time")
        if date and time:
            date_time = datetime.combine(date, time)
            cleaned_data["date_time"] = timezone.make_aware(date_time)

        return cleaned_data
