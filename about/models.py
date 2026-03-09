from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from modelcluster.fields import ParentalKey


class FormField(AbstractFormField):
    page = ParentalKey(
        "AboutPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )


class AboutPage(AbstractEmailForm):

    body = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    # add these
    to_address = models.CharField(max_length=255, blank=True)
    from_address = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
    ]

    promote_panels = Page.promote_panels

    settings_panels = Page.settings_panels + [
        FieldPanel("to_address"),
        FieldPanel("from_address"),
        FieldPanel("subject"),
    ]