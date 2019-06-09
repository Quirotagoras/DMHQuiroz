from django.db import models

class Product(models.Model):

    presentaciones = (
        ('Tab','Tabletas'),
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



    )


    unidades=(
        ('mg','miligramos'),
        ('g','gramos'),
        ('ml','mililitros'),


    )
    cbarras=models.PositiveIntegerField()
    subcuenta= models.CharField(max_length=100)
    nombre_comercial=models.CharField(max_length=200)
    nombre_activo=models.CharField(max_length=200)
    presentacion=models.CharField(choices=presentaciones,max_length=20,default='Tab')
    cantidad_pastillas = models.PositiveIntegerField()

    unidad_medida=models.CharField(choices=unidades,max_length=20)
    precio_max_pub=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_comercial + " " + self.unidad_medida+" "+ self.presentacion
