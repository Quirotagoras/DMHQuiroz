from django import forms
from .models import Doctor
from django.forms import ModelForm

class DoctorForm(ModelForm):


    class Meta:
        model = Doctor
        fields = ['first_name','last_name','last_name2','cedula','telefono','calle_num','cp']

        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder':'Inserte nombres de el doctor'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Inserte apellido paterno de el doctor'}),
            'last_name2': forms.TextInput(attrs={'placeholder': 'Inserte apellido materno de el doctor'}),
            'cedula': forms.TextInput(attrs={'placeholder': 'Inserte cedula de el doctor'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Inserte telefono de el doctor'}),
            'calle_num': forms.TextInput(attrs={'placeholder': 'Inserte calle y numero donde ejerce  el doctor'}),
            'cp': forms.TextInput(attrs={'placeholder': 'Inserte codigo postal donde ejerce  el doctor'}),

        }

        def is_valid(self):
            cd = self.cleaned_data
            if(cd['first_name'] and cd['last_name']and cd['last_name2'] and cd['cedula'] and cd['telefono'] and cd['calle_num'] and cd['cp']):
                return True
            else:
                return False






