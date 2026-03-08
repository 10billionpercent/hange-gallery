from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import PageChooserBlock


class ArtworkLinkBlock(blocks.StructBlock):
    artwork = PageChooserBlock(page_type="gallery.ArtworkPage")

    class Meta:
        icon = "image"
        label = "Artwork"


class MonthSectionBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    artworks = blocks.ListBlock(ArtworkLinkBlock())

    class Meta:
        icon = "folder-open-inverse"
        label = "Month Section"