from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Gerente,Capturista

class UsersAdmin(admin.ModelAdmin):
    pass
admin.site.register(Gerente,UsersAdmin)
admin.site.register(Capturista,UsersAdmin)


