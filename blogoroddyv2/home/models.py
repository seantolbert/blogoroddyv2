from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks

class HomePage(Page):
    headline = models.CharField(max_length=100, blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('headline'),
    ]

class AboutPage(Page):
    name = models.CharField(max_length=100, blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('name')
    ]