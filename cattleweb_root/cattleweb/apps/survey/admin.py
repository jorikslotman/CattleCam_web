from django.contrib import admin
from .models import Survey,Question,Answer,VisitEvent

# Register your models here.
admin.site.register([Survey,Question,VisitEvent])