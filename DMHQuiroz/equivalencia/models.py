from django.db import models
from products.models import Product

class Equivalencia(models.Model):
    cbarras=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cbarras1')
    descripcion = models.CharField(max_length=50)
    cbarras_equivalente = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='cbarras2')
    descripcion_equivalente = models.CharField(max_length=50)



