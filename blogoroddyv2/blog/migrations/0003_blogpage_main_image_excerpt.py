# Generated by Django 4.0.2 on 2022-02-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpage_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='main_image_excerpt',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
