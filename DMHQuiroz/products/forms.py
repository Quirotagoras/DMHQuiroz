from django.forms import ModelForm
from .models import Product
from django import forms



class formRegisterProduct(ModelForm):




    class Meta:
       model = Product
       fields = ['cbarras','subcuenta','nombre_comercial','nombre_activo','presentacion','cantidad_pastillas','unidad_medida','precio_max_pub']


       widgets = {
           'required' : True,
           'cbarras': forms.TextInput(attrs={'placeholder': 'Inserte Codigo de barras aqui','lab':'Codigo de Barras'}),
           'subcuenta': forms.TextInput(attrs={'placeholder': 'Inserte Subcuenta aqui'}),
           'nombre_comercial': forms.TextInput(attrs={'placeholder': 'Inserte Nombre comercial aqui'}),
           'nombre_activo': forms.TextInput(attrs={'placeholder': 'Inserte Nombre activo aqui'}),
           'cantidad_pastillas': forms.TextInput(attrs={'placeholder': 'Inserte Cantidad de pastillas en caja aqui'}),
           'precio_max_pub': forms.TextInput(attrs={'placeholder': 'Inserte Precio maximo al publico aqui'}),

       }

    def clean(self):
        cleaned_data = super().clean()
        cbarras = cleaned_data.get("cbarras")
        if cbarras:
            try:
                Product.objects.get(cbarras=cbarras)
                raise forms.ValidationError("Codigo de barras existente. Intente otravez")

            except Product.DoesNotExist:
                pass

