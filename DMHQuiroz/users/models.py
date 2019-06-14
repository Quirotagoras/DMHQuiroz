from django.db import models
from farmacia.models import Farmacia
from django.contrib.auth.models import User
# Create your models here.

class Gerente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    telefono = models.BigIntegerField()
    farmacia = models.OneToOneField(Farmacia,on_delete=models.CASCADE)
    is_active = models.BooleanField()


class Capturista(models.Model):
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telefono = models.BigIntegerField()
    email = models.EmailField()
    farmacia = models.ForeignKey(Farmacia, on_delete=models.CASCADE)
    is_active = models.BooleanField()



