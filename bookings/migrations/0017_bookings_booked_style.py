# Generated by Django 4.2.7 on 2023-12-10 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("styles", "0001_initial"),
        ("bookings", "0016_remove_newscomments_post_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookings",
            name="booked_style",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="booking",
                to="styles.stylesavailable",
            ),
            preserve_default=False,
        ),
    ]
