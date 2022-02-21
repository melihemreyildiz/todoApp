from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Groups)
admin.site.register(models.ToDos)