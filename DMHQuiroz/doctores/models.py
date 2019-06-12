from django.db import models
from farmacia.models import Farmacia


estado_choices= [
    ('AGS','Aguascalientes'),
    ('BC','Baja California'),
    ('BCS','Baja California Sur'),
    ('CAMP','Campeche'),
    ('CHIA','Chiapas'),
    ('CHIH','Chihuahua'),
    ('COA','Coahuila'),
    ('COL','Colima'),
    ('DUR','Durango'),
    ('EDOMEX','Estado de Mexico'),
    ('GTO','Guanajuato'),
    ('GRRO','Guerrero'),
    ('HGO','Hidalgo'),
    ('JAL','Jalisco'),
    ('MICH','Michoacan'),
    ('MOR','Morelos'),
    ('NAY','Nayarit'),
    ('NL','Nuevo Leon'),
    ('OAX','Oaxaca'),
    ('PUE','Puebla'),
    ('QRO','Queretaro'),
    ('QUROO','Quintana Roo'),
    ('SLP','San Luis Potosi'),
    ('SIN','Sinaloa'),
    ('SON','Sonora'),
    ('TAB','Tabasco'),
    ('TAM','Tamaulipas'),
    ('TLAX','Tlaxcala'),
    ('VER','Veracruz'),
    ('YUC','Yucatan'),
    ('ZAC','Zacatecas')

]

class Doctor(models.Model):
    first_name=models.CharField("Nombre",max_length=50)
    farmacia = models.ForeignKey(Farmacia,on_delete=models.CASCADE)#se tiene que cambiar a llave foranea
    last_name = models.CharField('Apellido Paterno',max_length=50)
    last_name2 = models.CharField('Apellido Materno',max_length=50)
    cedula = models.CharField('Cedula Profesional',max_length=50,unique=True)
    telefono = models.BigIntegerField()
    rfc = models.CharField(max_length=50,unique=True)
    calle_num = models.CharField("Calle y numero",max_length=100)
    estado = models.CharField(max_length=100,choices=estado_choices)
    municipio = models.CharField(max_length=100)
    cp = models.CharField('Codigo Postal',max_length=10)

    def __str__(self):


        return self.first_name + " " + self.last_name