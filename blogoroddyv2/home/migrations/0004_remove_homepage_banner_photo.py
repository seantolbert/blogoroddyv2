# Generated by Django 4.0.2 on 2022-02-15 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_banner_photo_homepage_excerpt_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='banner_photo',
        ),
    ]
