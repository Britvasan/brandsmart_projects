from django.core.management.base import BaseCommand
from card_app.models import SocialmediaTable

class Command(BaseCommand):
    help = "Insert social media data into SocialmediaTable"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚡ Deleting old social media data..."))
        SocialmediaTable.objects.all().delete()

        tasks = [
            ('linkedin_connection', 'No. of connections acquired on LinkedIn'),
            ('twitter_connection', 'No. of connections acquired on Twitter'),
            ('instagram_connection', 'No. of connections acquired on Instagram'),
            ('facebook_connection', 'No. of connections acquired on Facebook'),
        ]

        for task in tasks:
            SocialmediaTable.objects.create(socialmedia_tasks=task[1])

        self.stdout.write(self.style.SUCCESS("✅ Successfully inserted social media data!"))