from django.db import models

from django.shortcuts import render
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.models import Image
from modelcluster.fields import ParentalKey


class FormField(AbstractFormField):
    page = ParentalKey(
        "AboutPage",
        on_delete=models.CASCADE,
        related_name="form_fields",
    )

class AboutPage(AbstractEmailForm):
    body = RichTextField(blank=True)
    success_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    success_text = RichTextField(blank=False)

    error_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
    )
    error_text = RichTextField(blank=False)

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

    def render_landing_page(self, request, form_submission=None, *args, **kwargs):
        context = self.get_context(request)
        context['form_submission'] = form_submission
        context['is_error'] = False if form_submission else True
        
        return render(
            request,
            self.get_landing_page_template(request),
            context
        )

    content_panels = Page.content_panels + [
        "body",
        "use_modal_form",
        "modal_button_text",
        InlinePanel("form_fields", label="Form fields"),
        "success_text",
        "success_image",
        "error_text",
        "error_image"
    ]

    promote_panels = Page.promote_panels

    settings_panels = Page.settings_panels + [
        FieldPanel("to_address"),
        FieldPanel("from_address"),
        FieldPanel("subject"),
    ]