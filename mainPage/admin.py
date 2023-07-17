from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Tedarikci)
admin.site.register(models.Hammadde)
admin.site.register(models.MalAlim)
# admin.site.register(models.Alimlar_Kirilim)
admin.site.register(models.Kantar)