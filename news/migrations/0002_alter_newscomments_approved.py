# Generated by Django 4.2.7 on 2023-12-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newscomments",
            name="approved",
            field=models.IntegerField(
                choices=[(0, "Not Approved"), (1, "Approved")], default=0
            ),
        ),
    ]