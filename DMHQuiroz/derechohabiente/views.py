from .forms import DerechoHabienteForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import DerechoHabiente
from django.core.exceptions import ValidationError

def RegisterDerechoHabiente(request):


    if request.method == 'POST':
        form = DerechoHabienteForm(request.POST)
        if form.is_valid():
            new_derechohabiente = DerechoHabiente(

                ficha=form.cleaned_data.get('ficha'),
                codigo = form.cleaned_data.get('codigo'),
                org = form.cleaned_data.get('org'),

                nombre = form.cleaned_data.get('nombre'),
                calle_num = form.cleaned_data.get('calle_num'),
                colonia =form.cleaned_data.get('colonia'),
                estado = form.cleaned_data.get('estado'),
                municipio = form.cleaned_data.get('municipio'),
                cp = form.cleaned_data.get('cp'),
                telefono = form.cleaned_data.get('telefono'),
                email = form.cleaned_data.get('email'),

            )





            new_derechohabiente.save()
            return HttpResponseRedirect('/registeredDerechoHabiente/')
    else:
        form = DerechoHabienteForm()

    return render(request, '../templates/registerDerechoHabiente.html', {'Form': form})










