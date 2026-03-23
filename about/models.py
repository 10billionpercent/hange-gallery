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

    to_address = models.CharField(max_length=255, blank=True)
    from_address = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)

    use_modal_form = models.BooleanField(
        default=False, 
        verbose_name="Open form in a modal?"
    )
    modal_button_text = models.CharField(
        max_length=255, 
        blank=True, 
        default="Want a custom artwork? I do commissions too!",
        verbose_name="Modal Trigger Button Text"
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("use_modal_form"),
        FieldPanel("modal_button_text"),
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text"),
    ]

    promote_panels = Page.promote_panels

    settings_panels = Page.settings_panels + [
        FieldPanel("to_address"),
        FieldPanel("from_address"),
        FieldPanel("subject"),
    ]