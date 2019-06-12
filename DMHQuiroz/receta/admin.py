from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Receta

class RecetaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Receta,RecetaAdmin)


