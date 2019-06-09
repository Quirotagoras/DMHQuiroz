from django import forms
from .models import Doctor

class DoctorForm(forms.Form):
    first_name=forms.CharField(label="Nombre",max_length=100)
    last_name = forms.CharField(label="Apellido Paterno", max_length=100)
    last_name2 = forms.CharField(label="Apellido Materno", max_length=100)
    cedula=forms.CharField(label="Cedula Profesional", max_length=50)#
    telefono = forms.CharField(label="Telefono", max_length=50)
    rfc = forms.CharField(label="RFC", max_length=50)#12 a 13 caracteres
    calle_num=forms.CharField(label="Calle y numero",max_length=100)
    estado=forms.CharField(label="Estado donde ejerce", max_length=50)
    municipio=forms.CharField(label="Municipio donde ejerce", max_length=50)
    cp=forms.CharField(label="Codigo postal donde ejerce", max_length=10)

    def clean(self):
        cleaned_data = super().clean()
        cedula = cleaned_data.get("cedula")
        if cedula:
            try:
                Doctor.objects.get(cedula=cedula)
                raise forms.ValidationError("Cedula existente. Intente otravez")

            except Doctor.DoesNotExist:
                pass





