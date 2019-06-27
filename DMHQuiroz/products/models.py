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
    nombre_activo = models.CharField(max_length=200)
    nombre_comercial=models.CharField(max_length=200)
    presentacion = models.CharField(max_length=200)
    empaque = models.CharField(max_length=50)
    dcantidad = models.PositiveIntegerField()
    unidad_medida = models.CharField("Unidad de medida", choices=unidades, max_length=20)
    presenta = models.CharField(choices=presentaciones,max_length=100)
    gramaje = models.CharField(max_length=10)
    cve_farmacia = models.IntegerField()
    costo_venta = models.FloatField()
    costo_compra = models.FloatField()
    iva = models.IntegerField()
    proveedor = models.CharField(max_length=20)
    stock = models.IntegerField()
    modificacion = models.CharField(max_length=3,null=True)
    registro= models.CharField(max_length=20)
    grupo = models.CharField(max_length=2,null = True)
    laboratorio = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    tlc = models.CharField(max_length=3)
    pumpvp = models.FloatField()
    modalidad_real = models.CharField(max_length=2)




    def __str__(self):
        return self.nombre_activo+" " + self.nombre_comercial + " " + self.unidad_medida+" "+ self.presentacion
