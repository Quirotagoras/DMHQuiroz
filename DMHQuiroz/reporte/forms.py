from django import forms

class ExportXLSX(forms.Form):
    fechaDesde = forms.DateTimeField()
    fechaHasta = forms.DateTimeField()
    nombreArchivo = forms.CharField()

    class Meta:
        fields=['fechaDesde','fechaHasta','nombreArchivo']


    def is_valid(self):
        if self.data.get('fechaDesde') and self.data.get('fechaHasta')and self.data.get('nombreArchivo'):
            return True
        else:
            return False

    def clean(self):
        cd = self.data
        if not cd['fechaDesde']:
            raise forms.ValidationError('No llenaste el campo "Fecha Desde" ')
        if not cd['fechaHasta']:
            raise forms.ValidationError('No llenaste el campo "Fecha Hasta" ')
        if not cd['nombreArchivo']:
            raise forms.ValidationError('No llenaste el campo "Nombre de archivo" ')


