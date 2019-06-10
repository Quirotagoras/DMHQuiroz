from django.forms import ModelForm
from .models import Farmacia
from django import forms



class formRegisterFarmacia(ModelForm):




    class Meta:
       model = Farmacia
       fields = ['cve_admin','cve_admin2','nombre','telefono','calle_num','estado','municipio','cp']


       widgets = {
           'required' : True,
           'cve_admin': forms.TextInput(attrs={'placeholder':'Inserte clave de administrador aqui'}),
           'cve_admin2': forms.TextInput(attrs={'placeholder': 'Inserte clave 2 de administrador aqui'}),
            'nombre' : forms.TextInput(attrs={'placeholder':'Inserte nombre de farmacia aqui'}),
           'telefono' : forms.TextInput(attrs={'placeholder':'Inserte telefono de farmacia aqui'}),
           'calle_num' : forms.TextInput(attrs={'placeholder':'Inserte calle y numero donde se encuentra la farmacia aqui'}),
           'municipio' : forms.TextInput(attrs={'placeholder':'Inserte municipio aqui'}),
           'cp': forms.TextInput(attrs={'placeholder':'Inserte codigo postal aqui'}),


       }



