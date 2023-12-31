# Generated by Django 3.2.23 on 2023-11-21 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookings', '0006_stylesavailable_sample_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comments', to='bookings.newsposts')),
            ],
            options={
                'verbose_name': 'News Comment',
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='StylesComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=80)),
                ('comment_body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Style Comment',
                'ordering': ['created_on'],
            },
        ),
        migrations.AddField(
            model_name='stylesavailable',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='style_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stylesavailable',
            name='want_to_try',
            field=models.ManyToManyField(blank=True, related_name='want_to_try', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='stylescomments',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='style_comments', to='bookings.stylesavailable'),
        ),
    ]
