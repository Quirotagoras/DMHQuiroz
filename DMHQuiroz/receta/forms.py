from django.forms import ModelForm
from .models import Receta
from django import forms
from users.models import Gerente
from dal import autocomplete
from doctores.models import Doctor


class EquivalenciaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields=['equivalencia','equivalencia_obs']






class RecetaForm(forms.ModelForm):


    class Meta:
        model = Receta
        fields = ['folio_receta' , 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' ,'doctor','ficha_derechohabiente','cbarras','cantidad','has_Equivalencia']


        widgets = {


            'folio_receta': forms.TextInput(attrs={'placeholder':'Ingresar folio de receta'}),

            'fecha_expide': forms.DateInput(attrs={'class': 'datepicker',
                                                   }),

            'fecha_recibe': forms.DateInput(attrs={'class': 'datepicker'
                                                  }),
            'fecha_surte': forms.DateInput(attrs={'class': 'datepicker'}
                                                  ),

            'ficha_derechohabiente': forms.TextInput(),


        }

    def is_valid(self):

        if self.data['ficha_derechohabiente']  and self.data['cbarras']:
            return True
        else:
            return False



    def clean(self):
        folio = self.cleaned_data.get('folio_receta')
        if len(folio)!=12:
            raise forms.ValidationError('Folio debe de ser de 12 caracteres')







