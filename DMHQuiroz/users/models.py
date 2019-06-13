from django.db import models
from farmacia.models import Farmacia
from django.contrib.auth.models import User
# Create your models here.

class Gerente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telefono = models.BigIntegerField()
    farmacia = models.OneToOneField(Farmacia,on_delete=models.CASCADE)


class Capturista(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    telefono = models.BigIntegerField()
    farmacia = models.OneToOneField(Farmacia, on_delete=models.CASCADE)



