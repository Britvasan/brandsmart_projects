from django.core.management.base import BaseCommand
from card_app.models import MagazineTable

class Command(BaseCommand):
    help = "Insert magazine data into MagazineTable"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("⚡ Deleting old magazine data..."))
        MagazineTable.objects.all().delete()

        tasks = [
            ('magazine_designs', 'No. of pages designed for Magazine'),
            ('professionals_issue', 'No. of professionals prepared for the issue'),
            ('experts_issue', 'No. of experts prepared for the issue'),
            ('interview_questions', 'No. of Interview questionnaire prepared & sent'),
            ('new_advertisers', 'No. of new advertisers found & shared'),
            ('crossword_puzzles', 'No. of crossword puzzles prepared'),
        ]

        for task in tasks:
            MagazineTable.objects.create(magazine_tasks=task[1])

        self.stdout.write(self.style.SUCCESS("✅ Successfully inserted magazine data!"))
