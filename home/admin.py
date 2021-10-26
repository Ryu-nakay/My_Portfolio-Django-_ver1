from django.contrib import admin

# Register your models here.
from .models import NewsModel
from .models import AppModel
 
admin.site.register(NewsModel)
admin.site.register(AppModel)
