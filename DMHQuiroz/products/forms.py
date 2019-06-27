from django.forms import ModelForm
from .models import Product
from django import forms



class formRegisterProduct(ModelForm):


    class Meta:
       model = Product
       fields = ['cbarras','nombre_comercial','nombre_activo','presentacion','unidad_medida']


       widgets = {


       }



