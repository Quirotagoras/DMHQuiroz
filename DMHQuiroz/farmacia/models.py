from django.db import models

# Create your models here.

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

class Farmacia(models.Model):
    cve_admin = models.IntegerField("Clave de administrador",unique=True)
    cve_admin2 = models.CharField("Clave de administrador 2",max_length=50,unique=True)
    nombre = models.CharField(max_length=50)
    telefono = models.BigIntegerField("Telefono de farmacia")
    calle_num = models.CharField("Calle y numero",max_length=100)
    estado = models.CharField(choices=estado_choices,max_length=15)
    municipio=models.CharField(max_length=100)
    cp=models.PositiveIntegerField("Codigo Postal")



    def __str__(self):
        return self.nombre + " " + self.municipio





