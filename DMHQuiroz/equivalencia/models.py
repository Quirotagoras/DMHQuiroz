from django.db import models

class Equivalencia(models.Model):


    cbarras=models.PositiveIntegerField("Codgio de Barras")
    subcuenta= models.CharField(max_length=150)
    nombre_comercial=models.CharField(max_length=200)
    nombre_activo=models.CharField(max_length=200)
    presentacion=models.CharField(max_length=50)
    cantidad_pastillas = models.PositiveIntegerField()
    unidad_medida=models.CharField(max_length=50)
    precio_max_pub=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_comercial + " " + self.unidad_medida+" "+ self.presentacion
