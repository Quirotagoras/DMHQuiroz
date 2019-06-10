from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Farmacia

class FarmaciaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Farmacia,FarmaciaAdmin)


