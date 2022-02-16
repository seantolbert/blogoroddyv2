from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class BlogIndexPage(Page):
    
    def get_context(self, request):
        context = super().get_context(request)
        context['children'] = BlogPage.objects.child_of(self).live().order_by('-date')
        return context


class BlogPage(Page):
    date = models.DateField(blank=True, null=True)

    description = models.CharField(max_length=255, blank = True, null = True)
    
    main_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    main_image_excerpt = models.CharField(max_length=300, blank=True, null=True)

    content = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('content', blocks.RichTextBlock()),
            ('image', ImageChooserBlock())
        ], 
        blank=True, null=True
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('description'),
        ImageChooserPanel('main_image'),
        FieldPanel('main_image_excerpt'),
        StreamFieldPanel('content'),
    ]
