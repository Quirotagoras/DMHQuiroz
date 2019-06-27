from django.db import models
from products.models import Product

class Equivalencia(models.Model):
    cbarras=models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    cbarras_equivalente = models.CharField(max_length=200)
    descripcion_equivalente = models.CharField(max_length=200)
    cantidad_equivalente = models.CharField(max_length=50)


    def __str__(self):
        return self.cbarras_equivalente+" "+self.descripcion_equivalente


