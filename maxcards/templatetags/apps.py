from django.apps import AppConfig


class MaxcardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maxcards'
    
    def ready(self):
        import maxcards.templatetags

