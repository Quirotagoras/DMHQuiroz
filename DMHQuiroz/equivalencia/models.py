from django.db import models
from products.models import Product

class Equivalencia(models.Model):
    cbarras=models.TextField()
    descripcion = models.TextField()
    cbarras_equivalente = models.TextField()
    descripcion_equivalente = models.TextField()
    cantidad_equivalente = models.TextField()


    def __str__(self):
        return self.cbarras_equivalente+" "+self.descripcion_equivalente


