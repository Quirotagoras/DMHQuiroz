from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor,DoctorAdmin)


