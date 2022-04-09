from django.apps import AppConfig


# ?apps.py is the app's configuration.

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'
