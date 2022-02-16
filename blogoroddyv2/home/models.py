from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    headline = models.CharField(max_length=100, blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('headline'),
    ]