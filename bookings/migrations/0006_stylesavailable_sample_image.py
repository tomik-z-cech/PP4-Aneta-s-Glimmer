# Generated by Django 3.2.23 on 2023-11-21 18:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_auto_20231120_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='stylesavailable',
            name='sample_image',
            field=cloudinary.models.CloudinaryField(default='default_sample_image', max_length=255, verbose_name='image'),
        ),
    ]
