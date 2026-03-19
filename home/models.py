from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.admin.panels import FieldPanel


from wagtail.images import get_image_model_string

class HomePage(Page):
    body = RichTextField(blank=True)

    hero_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    content_panels = Page.content_panels + [
        "body",
        "hero_image",
    ]