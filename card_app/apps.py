from django.apps import AppConfig


class CardAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'card_app'

    def ready(self):
        import card_app.signals 
