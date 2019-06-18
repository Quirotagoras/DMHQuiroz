from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Equivalencia

class EquivalenciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Equivalencia,EquivalenciaAdmin)


