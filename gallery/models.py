from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.fields import StreamField
from wagtail.admin.panels import FieldPanel
from .blocks import MonthSectionBlock

class GalleryPage(Page):

    sections = StreamField(
    [
        ("month", MonthSectionBlock()),
    ],
    use_json_field=True,
    blank=True,
)

    content_panels = Page.content_panels + [
        FieldPanel("sections"),
    ]


class ArtworkPage(Page):
    parent_page_types = ["gallery.GalleryPage"]

    image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    description = RichTextField(blank=True)

    created_date = models.DateField()

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("description"),
        FieldPanel("created_date"),
    ]