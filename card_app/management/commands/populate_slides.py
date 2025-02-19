from django.core.management.base import BaseCommand
from card_app.models import SlidesTable

class Command(BaseCommand):
    help = "Insert slides data into SlidesTable"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚡ Deleting old slides data..."))
        SlidesTable.objects.all().delete()

        tasks = [
            ('business_slides', 'No. of slides prepared for Business team'),
            ('new_address', 'No. of new addresses collected'),
        ]

        for task in tasks:
            SlidesTable.objects.create(slides_tasks=task[1])

        self.stdout.write(self.style.SUCCESS("✅ Successfully inserted slides data!"))

