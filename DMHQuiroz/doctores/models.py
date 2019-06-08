from django.db import models

class Doctor(models.Model):
    first_name=models.CharField(max_length=50)
    farmacia = models. CharField(max_length=50)#se tiene que cambiar a llave foranea

    last_name = models.CharField(max_length=50)
    last_name2 = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50,unique=True)
    telefono = models.CharField(max_length=50)
    rfc = models.CharField(max_length=50,unique=True)
    calle_num = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    cp = models.CharField(max_length=10)

    def __str__(self):


        return "Dr. "+self.first_name + " " + self.last_name