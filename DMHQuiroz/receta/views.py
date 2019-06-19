from .forms import RecetaForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Receta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from farmacia.models import Farmacia
from .models import Receta
from users.models import Gerente,Capturista
from doctores.models import Doctor
from django import forms
from django.contrib.auth.decorators import login_required
from dal import autocomplete

def SuccessRegister(request):
    return render(request,'../templates/successReceta.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successRecetaGerente.html')





@login_required
def RegisterReceta(request,idEmpleado):
    if request.method == 'POST':
        print('entre a post')
        form = RecetaForm(request.POST)
        if form.is_valid():
            print('entre a valid')
            try:
                model = Capturista.objects.get(user_id=idEmpleado)
                username = model.user
                user_id = User.objects.get(username=username)

                id_farmacia = model.farmacia_id
                try:
                    Receta.objects.get(folio_receta=form.cleaned_data.get('folio_receta'),farmacia_id=id_farmacia)
                    return HttpResponseRedirect('/receta/'+str(idEmpleado))
                except Receta.DoesNotExist:
                    new_derechohabiente = Receta(
                        folio_receta=form.cleaned_data.get("folio_receta"),
                        status=form.cleaned_data.get("status"),
                        fecha_expide=form.cleaned_data.get("fecha_expide"),
                        fecha_recibe=form.cleaned_data.get("fecha_recibe"),
                        fecha_surte=form.cleaned_data.get("fecha_surte"),
                        doctor=form.cleaned_data.get("doctor"),
                        ficha_derechohabiente=form.cleaned_data.get("ficha_derechohabiente"),
                        cantidad=form.cleaned_data.get("cantidad"),
                        cbarras=form.cleaned_data.get("cbarras"),
                        farmacia=Farmacia.objects.get(id=id_farmacia),
                        equivalencia_cantidad=form.cleaned_data.get("equivalencia_cantidad"),
                        equivalencia_obs=form.cleaned_data.get("equivalencia_obs"),
                        creado=timezone.now(),
                        ultimamodif=timezone.now(),
                        empleado = user_id,

                    )
                    new_derechohabiente.save()



            except Capturista.DoesNotExist:
                #modelo de empleado
                pass


            return HttpResponseRedirect('/receta/registeredReceta/')

    else:
        form = RecetaForm()

    return render(request, '../templates/registerReceta.html', {'Form': form})


@login_required
def RegisterRecetaGerente(request,idEmpleado):
    if request.method == 'POST':
        print('entre a post')
        form = RecetaForm(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print('entre a valid')
            model = Gerente.objects.get(user_id=idEmpleado)
            username = model.user
            user_id = User.objects.get(username=username)
            id_farmacia = model.farmacia_id
            try:
                Receta.objects.get(folio_receta=form.cleaned_data.get('folio_receta'),farmacia_id=id_farmacia)
                return HttpResponseRedirect('/recetaGerente/'+str(idEmpleado)+'/Gerente')
            except Receta.DoesNotExist:
                new_derechohabiente = Receta(
                    folio_receta=form.cleaned_data.get("folio_receta"),
                    status=form.cleaned_data.get("status"),
                    fecha_expide=form.cleaned_data.get("fecha_expide"),
                    fecha_recibe=form.cleaned_data.get("fecha_recibe"),
                    fecha_surte=form.cleaned_data.get("fecha_surte"),
                    doctor=form.cleaned_data.get("doctor"),
                    ficha_derechohabiente=form.cleaned_data.get("ficha_derechohabiente"),
                    cantidad=form.cleaned_data.get("cantidad"),
                    cbarras=form.cleaned_data.get("cbarras"),
                    farmacia=Farmacia.objects.get(id=id_farmacia),
                    equivalencia_cbarras=form.cleaned_data.get("equivalencia_cbarras"),
                    equivalencia_cantidad=form.cleaned_data.get("equivalencia_cantidad"),
                    equivalencia_obs=form.cleaned_data.get("equivalencia_obs"),
                    creado=timezone.now(),
                    ultimamodif=timezone.now(),
                    empleado = user_id,

                    )
                new_derechohabiente.save()



            return HttpResponseRedirect('/receta/registeredRecetaGerente/')
        else:
            print('entre a not valid')

    else:
        print("entre")
        form = RecetaForm()



    return render(request, '../templates/registerRecetaGerente.html', {'Form': form})












