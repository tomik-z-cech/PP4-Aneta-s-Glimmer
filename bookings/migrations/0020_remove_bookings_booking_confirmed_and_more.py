# Generated by Django 4.2.7 on 2023-12-11 18:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bookings", "0019_bookings_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bookings",
            name="booking_confirmed",
        ),
        migrations.RemoveField(
            model_name="bookings",
            name="booking_done",
        ),
        migrations.AddField(
            model_name="bookings",
            name="booking_status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Confirmed"), (2, "Done")], default=0
            ),
        ),
    ]
