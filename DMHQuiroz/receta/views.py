from .forms import RecetaForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Receta
from django.core.exceptions import ValidationError
from django.utils import timezone

def RegisterReceta(request):


    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            new_derechohabiente = Receta(

                folio_receta=form.cleaned_data.get("folio_receta"),
                status = form.cleaned_data.get("status"),
                fecha_expide = form.cleaned_data.get("fecha_expide"),
                fecha_recibe = form.cleaned_data.get("fecha_recibe"),
                fecha_surte = form.cleaned_data.get("fecha_surte"),
                doctor = form.cleaned_data.get("doctor"),
                ficha_derechohabiente = form.cleaned_data.get("ficha_derechohabiente"),
                cantidad = form.cleaned_data.get("cantidad"),
                cbarras = form.cleaned_data.get("cbarras"),
                farmacia = form.cleaned_data.get("farmacia"),
                equivalencia_cbarras = form.cleaned_data.get("equivalencia_cbarras"),
                equivalencia_cantidad = form.cleaned_data.get("equivalencia_cantidad"),
                equivalencia_obs = form.cleaned_data.get("equivalencia_obs"),
                creado = timezone.now(),
                ultimamodif = timezone.now(),

            )





            new_derechohabiente.save()
            return HttpResponseRedirect('/registeredReceta/')
    else:
        form = RecetaForm()

    return render(request, '../templates/registerReceta.html', {'Form': form})










