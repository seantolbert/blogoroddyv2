# Generated by Django 4.0.2 on 2022-03-02 04:15

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True),
        ),
    ]