# Generated by Django 4.0.2 on 2022-03-02 02:14

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpage_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='content',
        ),
        migrations.AddField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('content', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True, null=True),
        ),
    ]