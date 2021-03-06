from django.forms import ModelForm
from .models import DerechoHabiente
from django import forms


class DerechoHabienteForm(ModelForm):

    class Meta:
        model = DerechoHabiente
        fields = ['ficha','codigo','org','nombre','calle_num','colonia','cp','telefono','email']


        widgets = {
            'ficha': forms.TextInput(attrs={'placeholder' :'Inserte ficha de derecho habiente aqui'}),
            'codigo': forms.TextInput(attrs={'placeholder': 'Inserte codigo de derecho habiente aqui'}),
            'org': forms.NumberInput(attrs={'placeholder': 'Inserte organizacion de derecho habiente aqui'}),
            'nombre': forms.TextInput(attrs={'placeholder': 'Inserte nombre de derecho habiente aqui'}),
            'calle_num': forms.TextInput(attrs={'placeholder': 'Inserte calle y numero de residencia  de derecho habiente aqui'}),
            'colonia': forms.TextInput(
                attrs={'placeholder': 'Inserte colonia de residencia  de derecho habiente aqui'}),
            'cp': forms.TextInput(attrs={'placeholder': 'Inserte cp de residencia de derecho habiente aqui'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Inserte telefono de derecho habiente aqui'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Inserte email de derecho habiente aqui'}),

        }

        def is_valid(self):
            cd = self.cleaned_data
            if (cd['ficha'] and cd['codigo'] and cd['org'] and cd['nombre'] and cd['calle_num'] and cd['colonia'] and cd['cp'] and cd['telefono'] and cd['email']):
                return True
            else:
                return False


    #def clean(self):
     #   cleaned_data = super().clean()
      #  ficha = cleaned_data.get("ficha")
       # codigo= cleaned_data.get("codigo")
        #if ficha and codigo:
         #   print('entre en orimer if')
          #  try:
           #     DerechoHabiente.objects.get(ficha=ficha, codigo = codigo)
            #    print('entre en repetido')
             #   raise forms.ValidationError("Ficha en combinacion con Codigo existente. Intente otravez")

            #except DerechoHabiente.DoesNotExist:
             #   print('entre a no existe')
              #  pass


