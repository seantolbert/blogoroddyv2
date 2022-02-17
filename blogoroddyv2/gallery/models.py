from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import StreamFieldPanel

class GalleryPage(Page):
    gallery_photo = StreamField([
        ('image', ImageChooserBlock()),
        ('description', blocks.CharBlock())
    ], 
    blank=True,
    null=True
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('gallery_photo')
    ]

