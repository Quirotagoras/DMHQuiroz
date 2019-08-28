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

# Create your models here.

class DerechoHabiente(models.Model):
    ficha = models.PositiveIntegerField()
    codigo = models.PositiveIntegerField()
    org = models.CharField(max_length=50,blank=True,null=True)
    farmacia = models.ForeignKey(Farmacia,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    calle_num = models.CharField("Calle y numero",max_length=100)
    colonia = models.CharField(max_length=100)
    estado = models.CharField(max_length=100,choices=estado_choices)
    municipio = models.CharField(max_length=50)
    cp = models.PositiveIntegerField("Codigo postal")
    telefono = models.BigIntegerField()
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre
