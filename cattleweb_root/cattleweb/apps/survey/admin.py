from django.contrib import admin
from .models import Survey,Question,Answer,Response

# Register your models here.
admin.site.register([Survey,Question,Answer,Response])