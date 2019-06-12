from django.forms import ModelForm
from .models import Receta
from django import forms


class RecetaForm(ModelForm):

    class Meta:
        model = Receta

        fields = ['folio_receta' , 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' , 'doctor' ,'ficha_derechohabiente','farmacia','cbarras','cantidad','equivalencia_cbarras','equivalencia_cantidad','equivalencia_obs']

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
    def clean(self):
        cleaned_data = super().clean()
        folio_receta = cleaned_data.get("folio_receta")
        if folio_receta:
            try:
                Receta.objects.get(folio_receta=folio_receta)
                raise forms.ValidationError("Folio existente. Intente otravez")

            except Receta.DoesNotExist:
                pass


