from django.core.management.base import BaseCommand
from card_app.models import OthersTable

class Command(BaseCommand):
    help = "Insert other tasks data into OthersTable"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚡ Deleting old other tasks data..."))
        OthersTable.objects.all().delete()

        tasks = [
            ('new_plugins', 'New Plugins designed'),
            ('other_tasks', 'Other tasks worked out'),
        ]

        for task in tasks:
            OthersTable.objects.create(other_tasks=task[1])

        self.stdout.write(self.style.SUCCESS("✅ Successfully inserted other tasks data!"))
