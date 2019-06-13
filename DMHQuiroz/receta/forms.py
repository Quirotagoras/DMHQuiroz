from django.forms import ModelForm
from .models import Receta
from django import forms


class RecetaForm(ModelForm):

    class Meta:
        model = Receta

        fields = ['folio_receta' , 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' ,'doctor','ficha_derechohabiente','cbarras','cantidad','equivalencia_cbarras','equivalencia_cantidad','equivalencia_obs']

        widgets = {
            'required' : True,
            'folio_receta' : forms.TextInput(attrs={'placeholder':'Ingresar folio de receta'}),

            'fecha_expide' : forms.DateInput(attrs={'class': 'datepicker',
                                                    'placeholder': 'formato: mm/dd/yyyy'}),
            'fecha_recibe': forms.DateInput(attrs={'class': 'datepicker',
                                                   'placeholder': 'formato: mm/dd/yyyy'}),
            'fecha_surte': forms.DateInput(attrs={'class': 'datepicker',
                                                   'placeholder': 'formato: mm/dd/yyyy'}),







        }



