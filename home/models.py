from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, PageChooserPanel 

class HomePage(Page):
    body = RichTextField(blank=True)
    hero_image = models.ForeignKey(
        "wagtailimages.Image", 
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    cta_text = models.CharField(
        max_length=50, 
        default="Enter Hange Gallery",
        verbose_name="CTA button text",
        help_text="Text to display on the CTA button"
    )
    
    hero_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Page that opens on clicking hero image"
    )

    cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Page that opens on clicking CTA button"
    )

    content_panels = Page.content_panels + [
       FieldPanel("body"),
       FieldPanel("hero_image"),
       FieldPanel("cta_text"), 
       PageChooserPanel("hero_link"),
       PageChooserPanel("cta_link"),
    ]