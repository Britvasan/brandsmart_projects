from django.db.models.signals import pre_save
from django.dispatch import receiver
from card_app.models import NewsTable, NewsActivity

@receiver(pre_save, sender=NewsTable)
def track_news_changes(sender, instance, **kwargs):
    try:
        old_instance = NewsTable.objects.get(pk=instance.pk)
        NewsActivity.objects.create(
            task=instance,
            action="Modified",
            prev_today_tasks=old_instance.today_tasks,
            prev_total_tasks=old_instance.total_tasks
        )
    except NewsTable.DoesNotExist:
        pass  # This happens when creating a new task, so ignore it
