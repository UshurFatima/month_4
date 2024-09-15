from django.contrib import admin
from . import models

# регистрируем модель, чтоб высвечиваось где админ
admin.site.register(models.Post)
admin.site.register(models.Review)