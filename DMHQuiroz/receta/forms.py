from django.forms import ModelForm
from .models import Receta
from django import forms
from users.models import Gerente


class RecetaForm(ModelForm):

    class Meta:
        model = Receta
        fields = ['folio_receta' , 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' ,'doctor','ficha_derechohabiente','cbarras','cantidad','equivalencia_cbarras','equivalencia_cantidad','equivalencia_obs']

        widgets = {


            'folio_receta': forms.TextInput(attrs={'placeholder':'Ingresar folio de receta'}),

            'fecha_expide': forms.DateInput(attrs={'class': 'datepicker',
                                                    'placeholder': 'formato: mm/dd/yyyy'}),

            'fecha_recibe': forms.DateInput(attrs={'class': 'datepicker',
                                                   'placeholder': 'formato: mm/dd/yyyy'}),
            'fecha_surte': forms.DateInput(attrs={'class': 'datepicker',
                                                   'placeholder': 'formato: mm/dd/yyyy'}),





        }

    def clean(self):
        folio = self.cleaned_data.get('folio_receta')
        if len(folio)!=12:
            raise forms.ValidationError('Folio debe de ser de 12 caracteres')







