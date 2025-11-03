from django.contrib import admin
from .models import Bulletin, News
# Register your models here.

admin.site.register(News)
admin.site.register(Bulletin)