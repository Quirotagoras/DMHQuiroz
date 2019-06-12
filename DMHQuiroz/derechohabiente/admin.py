from django.contrib import admin
from .models import DerechoHabiente

class DerechohabienteConfig(admin.ModelAdmin):
    pass
admin.site.register(DerechoHabiente,DerechohabienteConfig)


