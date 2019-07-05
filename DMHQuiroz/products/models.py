from django.db import models


class Product(models.Model):

    presentaciones = [
        ('Tabletas','Tabletas'),
        ('Amp','Ampolletas'),
        ('Polv','Polvos'),
        ('Cap','Capsulas'),
        ('Pil','Pildoras'),
        ('Grag','Grageas'),
        ('Sup','Supositorios'),
        ('Ov','Ovulos'),
        ('Pom','Pomada'),
        ('Cre','Crema'),
        ('Sol','Soluciones'),
        ('Jar','Jarabes'),
        ('Col','Colirios'),
        ('Loc','Lociones'),
        ('Lin','Linimiento'),
        ('Eli','Elixir'),
        ('Ene','Enema'),
        ('Inha','Inhalaciones'),
        ('Aero','Aerosoles'),



    ]


    unidades=[
        ('mg','miligramos'),
        ('g','gramos'),
        ('ml','mililitros'),


    ]
    cbarras=models.BigIntegerField("Codgio de Barras",unique=True)
    ubicacion = models.CharField(max_length=100)
    nombre_activo = models.TextField()
    nombre_comercial=models.TextField()
    presentacion = models.TextField()
    empaque = models.CharField(max_length=50)
    dcantidad = models.FloatField()
    unidad_medida = models.CharField("Unidad de medida", choices=unidades, max_length=20)
    presenta = models.CharField(choices=presentaciones,max_length=100)
    gramaje = models.TextField()
    cve_farmacia = models.IntegerField()
    costo_venta = models.FloatField()
    costo_compra = models.FloatField()
    iva = models.IntegerField()
    proveedor = models.TextField()
    stock = models.IntegerField()
    modificacion = models.CharField(max_length=3,null=True)
    registro= models.CharField(max_length=20)
    grupo = models.CharField(max_length=2,null = True)
    laboratorio = models.TextField()
    pais = models.TextField
    tlc = models.CharField(max_length=10)
    pumpvp = models.FloatField()
    modalidad_real = models.CharField(max_length=10)




    def __str__(self):
        return self.nombre_activo+" " + self.nombre_comercial + " " + self.unidad_medida+" "+ self.presentacion
