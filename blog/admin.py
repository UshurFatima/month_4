from django.contrib import admin
from . import models

# регистрируем модель, чтоб высвеечивалась где админ
admin.site.register(models.Post)
