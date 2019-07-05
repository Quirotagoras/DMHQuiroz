from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import  Capturista


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contrasena")


class UserForm(ModelForm):
    password = forms.CharField(label='Contrasena', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasena', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Asegurese que las contrasenas coinciden ')
        return cd['password2']


class CapturistaForm(ModelForm):
    class Meta:
        model = Capturista
        fields = ('nombre','apellidos','telefono','email')












