from django.contrib import admin

# Register your models here.
from .models import NewsModel
from .models import AppModel
from .models import ProgramingCareerModel
from .models import QualificationModel
from .models import SchoolDaysModel

admin.site.register(NewsModel)
admin.site.register(AppModel)
admin.site.register(ProgramingCareerModel)
admin.site.register(QualificationModel)
admin.site.register(SchoolDaysModel)