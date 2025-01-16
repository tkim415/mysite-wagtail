from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True)
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('title'),
        FieldPanel('subtitle'),
        ImageChooserPanel('background_image'),
    ]