# Generated by Django 4.2.7 on 2023-12-10 17:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0017_bookings_booked_style"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookings",
            old_name="date",
            new_name="date_time",
        ),
        migrations.RemoveField(
            model_name="bookings",
            name="time",
        ),
    ]