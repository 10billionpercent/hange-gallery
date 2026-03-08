from django.core.management.base import BaseCommand
from wagtail.images.models import Image
from gallery.models import ArtworkPage, GalleryPage
from datetime import date


class Command(BaseCommand):
    help = "Create ArtworkPages for images that don't already have one"

    def handle(self, *args, **kwargs):

        gallery = GalleryPage.objects.first()

        if not gallery:
            self.stdout.write("No GalleryPage found.")
            return

        images = Image.objects.all()

        for img in images:

            # Skip images already used in an ArtworkPage
            if ArtworkPage.objects.filter(image=img).exists():
                continue

            page = ArtworkPage(
                title=img.title,
                image=img,
                created_date=date.today()
            )

            gallery.add_child(instance=page)
            page.save_revision().publish()

            self.stdout.write(f"Created page for {img.title}")

        self.stdout.write("Finished creating artwork pages.")