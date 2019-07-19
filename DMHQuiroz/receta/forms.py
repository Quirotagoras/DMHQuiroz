from django.forms import ModelForm
from .models import Receta
from django import forms
from users.models import Gerente
from dal import autocomplete
from doctores.models import Doctor
from .models import Receta


class EquivalenciaForm(forms.ModelForm):



    class Meta:
        model = Receta
        fields=['equivalencia','equivalencia_obs']



class FindRecetaForm(forms.Form):
    receta = forms.CharField()
    temp_id = forms.CharField()

    class Meta:
        fields=['receta']


    def is_valid(self):
        receta = self.data['receta']
        pk = self.data['temp_id']
        gerente = Gerente.objects.get(user_id=pk)
        farmacia = gerente.farmacia

        try:

            Receta.objects.get(folio_receta=receta, farmacia=farmacia)

            return True
        except Receta.DoesNotExist:

            return False


    def clean(self):
        receta  = self.cleaned_data.get('receta')
        pk = self.cleaned_data.get('temp_id')
        gerente = Gerente.objects.get(user_id=pk)
        farmacia = gerente.farmacia

        if Receta.objects.get(folio_receta=receta,farmacia=farmacia):
            raise self.ValidationError('Ahuevo')
        else:
            raise self.ValidationError('Receta no existe.')



class RecetaFormEdit(forms.ModelForm):

    changeEquivalencia= forms.BooleanField()

    class Meta:
        model = Receta
        fields = [ 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' ,'doctor','ficha_derechohabiente','cbarras','cantidad','has_Equivalencia']


        widgets = {


            'folio_receta': forms.TextInput(attrs={'placeholder':'Ingresar folio de receta'}),

            'fecha_expide': forms.DateInput(attrs={'class': 'datepicker',
                                                   }),

            'fecha_recibe': forms.DateInput(attrs={'class': 'datepicker'
                                                  }),
            'fecha_surte': forms.DateInput(attrs={'class': 'datepicker'}
                                                  ),



        }

    def is_valid(self):
        folio = self.cleaned_data.get('folio_receta')
        cd = self.cleaned_data
        if self.data['ficha_derechohabiente']  and self.data['cbarras']:
            return True

        else:
            return False



class RecetaForm(forms.ModelForm):
    folio2 = forms.CharField(label='Repetir Contrasena')
    nur2 = forms.CharField(label="Repetir Nur")



    class Meta:
        model = Receta
        fields = ['nur','folio_receta' , 'status' , 'fecha_expide' , 'fecha_recibe' , 'fecha_surte' ,'doctor','ficha_derechohabiente','cbarras','cantidad','has_Equivalencia']


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
        folio = self.cleaned_data.get('folio_receta')
        nur = self.cleaned_data.get('nur')
        cd = self.cleaned_data
        if self.data['nur'] and self.data['ficha_derechohabiente']  and self.data['cbarras'] and len(folio)==7 and self.data['cantidad'] and (cd['folio2'] == cd['folio_receta'])and len(nur)==12 and (cd['nur2'] == cd['nur']):
            return True

        else:
            return False



    def clean(self):
        cd = self.cleaned_data
        folio = self.cleaned_data.get('folio_receta')
        nur = self.cleaned_data.get('nur')
        if len(folio)!=7:
            raise forms.ValidationError('Folio de receta debe de ser de 7 caracteres')

        if len(nur)!=12:
            raise forms.ValidationError('NUR debe de ser de 12 caracteres')

        if cd['folio2'] != cd['folio_receta']:
            raise forms.ValidationError('Asegurese que los folios de receta coinciden ')

        if cd['nur2'] != cd['nur']:
            raise forms.ValidationError('Asegurese que NUR coincide ')
















