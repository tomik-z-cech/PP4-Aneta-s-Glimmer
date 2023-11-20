# Generated by Django 3.2.23 on 2023-11-20 16:44

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('profile_picture', cloudinary.models.CloudinaryField(default='default_artist_pp', max_length=255, verbose_name='image')),
                ('bio', models.TextField()),
                ('public_profile', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('rating', models.FloatField(default=5.0)),
                ('bookings_total', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='StylesAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=100)),
                ('style_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', cloudinary.models.CloudinaryField(default='default_pp', max_length=255, verbose_name='image')),
                ('marketing', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('heading_image', cloudinary.models.CloudinaryField(default='default_heading_image', max_length=255, verbose_name='image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.IntegerField(choices=[(0, 'Not Published'), (1, 'Published')], default=0)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='news_likes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='bookings.news')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('time', models.DateTimeField()),
                ('booking_confirmed', models.BooleanField(default=False)),
                ('booking_done', models.BooleanField(default=False)),
                ('booked_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='bookings.artists')),
            ],
        ),
        migrations.AddField(
            model_name='artists',
            name='styles',
            field=models.ManyToManyField(to='bookings.StylesAvailable'),
        ),
    ]
