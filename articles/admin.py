from django.contrib import admin
from .models import Article

# ? Register your models here to the admin site.
# ?admin.py is how we associate the app with the admin page.

admin.site.register(Article)
