from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class GalleryPage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    excerpt = models.CharField(max_length=300, blank=True, null=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('excerpt')
    ]
