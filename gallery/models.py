from django.db import models
import random
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.models import Image
from wagtail.fields import StreamField
from .blocks import MonthSectionBlock

class GalleryPage(Page):

    sections = StreamField(
    [
        ("month", MonthSectionBlock()),
    ],
    use_json_field=True,
    blank=True,
)

    content_panels = Page.content_panels + ["sections"]


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

    suggested_count = models.IntegerField(
        default=3,
        help_text='Number of artworks to suggest'
    )

    content_panels = Page.content_panels + ["image", "description","created_date","suggested_count"]
    def get_suggested_artworks(self):

        pages = list(
            ArtworkPage.objects.live().exclude(id=self.id)
        )

        return random.sample(pages, min(len(pages), self.suggested_count))

    def get_context(self, request):

        context = super().get_context(request)

        context["suggested_artworks"] = self.get_suggested_artworks()

        return context