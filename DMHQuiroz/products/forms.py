from django.forms import ModelForm
from .models import Product
from django import forms

PRESENTACIONES_CHOICES = [
    ('Tab', 'Tabletas'),
    ('Amp', 'Ampolletas'),
    ('Polv', 'Polvos'),
    ('Cap', 'Capsulas'),
    ('Pil', 'Pildoras'),
    ('Grag', 'Grageas'),
    ('Sup', 'Supositorios'),
    ('Ov', 'Ovulos'),
    ('Pom', 'Pomada'),
    ('Cre', 'Crema'),
    ('Sol', 'Soluciones'),
    ('Jar', 'Jarabes'),
    ('Col', 'Colirios'),
    ('Loc', 'Lociones'),
    ('Lin', 'Linimiento'),
    ('Eli', 'Elixir'),
    ('Ene', 'Enema'),
    ('Inha', 'Inhalaciones'),
    ('Aero', 'Aerosoles'),

]

UNIDADES_CHOICES = [
    ('mg', 'miligramos'),
    ('g', 'gramos'),
    ('ml', 'mililitros'),

]

class formRegisterProduct(ModelForm):




    class Meta:
       model = Product
       fields = ['cbarras','subcuenta','nombre_comercial','nombre_activo','presentacion','cantidad_pastillas','unidad_medida','precio_max_pub']



    def clean(self):
        cleaned_data = super().clean()
        cbarras = cleaned_data.get("cbarras")
        if cbarras:
            try:
                Product.objects.get(cbarras=cbarras)
                raise forms.ValidationError("Codigo de barras existente. Intente otravez")

            except Product.DoesNotExist:
                pass

