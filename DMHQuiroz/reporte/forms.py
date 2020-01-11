from django import forms

class ExportXLSX(forms.Form):
    fechaDesde = forms.DateTimeField()
    fechaHasta = forms.DateTimeField()
    con_Iva = forms.BooleanField()
    sin_Iva = forms.BooleanField()
    nombreArchivo = forms.CharField()
    nombreProveedor = forms.CharField()
    auxiliarTecnico = forms.CharField()
    ficha = forms.CharField()


    class Meta:
        fields=['fechaDesde','fechaHasta','nombreArchivo','con_Iva','sin_Iva','auxiliarTecnico','ficha']


    def is_valid(self):
        if self.data.get('fechaDesde') and self.data.get('nombreProveedor') and self.data.get('fechaHasta')and self.data.get('nombreArchivo') and (self.data.get('con_Iva')or(self.data.get('sin_Iva')))and self.data.get('auxiliarTecnico') and self.data.get('ficha'):
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
        if not cd['auxiliarTecnico']:
            raise forms.ValidationError('No llenaste el campo "Auxiliar técnico" ')
        if not cd['ficha']:
            raise forms.ValidationError('No llenaste el campo "Ficha" ')
        if not cd['nombreProveedor']:
            raise forms.ValidationError('No llenaste el campo "Ficha" ')
        if self.data.get('con_Iva') == None and self.data.get('con_Iva') == None:
            raise forms.ValidationError('Debes elegir por lo menos una opcion de IVA ')





