from django.db import models
from products.models import Product
from doctores.models import Doctor
from derechohabiente.models import DerechoHabiente
from farmacia.models import Farmacia
from equivalencia.models import Equivalencia
from django.contrib.auth.models import User

# Create your models here.
class Receta(models.Model):
    nur = models.CharField('NUR',max_length=255,unique=True)
    folio_receta = models.CharField("Folio de Receta",max_length=255)
    fecha_expide = models.DateField("Fecha de expedicion")
    fecha_recibe = models.DateField("Fecha que recibe")
    fecha_surte = models.DateField("Fecha que surte")
    doctor = models.CharField(max_length=100)#se pone como char field por el tema del autocomplete
    ficha_derechohabiente = models.ForeignKey(DerechoHabiente,on_delete=models.CASCADE)
    cbarras = models.ForeignKey(Product,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    equivalencia = models.ForeignKey(Equivalencia,on_delete=models.CASCADE,blank=True,null=True)
    equivalencia_obs = models.TextField(max_length=300,blank=True,null=True)
    farmacia = models.ForeignKey(Farmacia,on_delete=models.CASCADE)
    creado = models.DateField()
    ultimamodif = models.DateField()
    empleado = models.ForeignKey(User,on_delete=models.CASCADE)
    has_Equivalencia = models.BooleanField(default=False)






