from django.core.management.base import BaseCommand
from card_app.models import NewsTable

class Command(BaseCommand):
    help = "Insert news data into NewsTable"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚡ Deleting old news data..."))
        NewsTable.objects.all().delete()

        tasks = [
            ('news_website', 'No. of news published on Website'),
            ('news_socialmedia', 'No. of news published on Social Media'),
            ('newsletter_subscription', 'No. of subscriptions done for Newsletter'),
            ('email_newsletter', 'Newsletter prepared for customers via Email'),
        ]

        for task in tasks:
            NewsTable.objects.create(news_tasks=task[1])

        self.stdout.write(self.style.SUCCESS("✅ Successfully inserted news data!"))
