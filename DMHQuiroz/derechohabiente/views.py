from .forms import DerechoHabienteForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import DerechoHabiente
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from users.models import Capturista,Gerente
from django.contrib.auth.models import User
from farmacia.models import Farmacia
from .models import  DerechoHabiente
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def DerechoList (request,idEmpleado):
    model = Gerente.objects.get(user_id=idEmpleado)
    id_farmacia = model.farmacia_id
    habientes_list = DerechoHabiente.objects.filter(farmacia=id_farmacia)
    page = request.GET.get('page',1)
    paginator = Paginator(habientes_list,10)
    try:
        habientes = paginator.page(page)
    except PageNotAnInteger:
        habientes = paginator.page(1)
    except EmptyPage:
        habientes = paginator.page(paginator.num_pages)

    return render(request,'../templates/listDerecho.html',{'habientes':habientes})



def SuccessRegister(request):
    return render(request,'../templates/successDerecho.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successDerechoGerente.html')

def editDerecho(request,idEmpleado,idDerecho):
    habiente = DerechoHabiente.objects.get(pk=idDerecho)

    if request.method=='POST':
        form = DerechoHabienteForm(request.POST)
        if form.is_valid():
            habiente.ficha = form.cleaned_data.get('ficha')
            habiente.codigo = form.cleaned_data.get('codigo')
            habiente.org = form.cleaned_data.get('org')

            habiente.nombre = form.cleaned_data.get('nombre')
            habiente.calle_num = form.cleaned_data.get('calle_num')
            habiente.colonia = form.cleaned_data.get('colonia')

            habiente.cp = form.cleaned_data.get('cp')
            habiente.telefono = form.cleaned_data.get('telefono')
            habiente.email = form.cleaned_data.get('email')
            habiente.save()
            return HttpResponseRedirect('/derechoHabiente/registeredDerechoHabienteGerente/')
    else:
        form = DerechoHabienteForm(request.POST)


    context={'Form':form,'habiente':habiente}
    return render(request, '../templates/editDerechoHabiente.html',context)


@login_required
def RegisterDerechoHabiente(request,idEmpleado):
    if request.method == 'POST':
        form = DerechoHabienteForm(request.POST)
        model = Capturista.objects.get(user_id=idEmpleado)

        id_farmacia = model.farmacia_id
        farmacia = Farmacia.objects.get(id=id_farmacia)
        farmacia_estado = farmacia.estado
        farmacia_municipio = farmacia.municipio

        if form.is_valid():
            new_derechohabiente = DerechoHabiente(

                ficha=form.cleaned_data.get('ficha'),
                codigo=form.cleaned_data.get('codigo'),
                org=form.cleaned_data.get('org'),
                farmacia=farmacia,
                nombre=form.cleaned_data.get('nombre'),
                calle_num=form.cleaned_data.get('calle_num'),
                colonia=form.cleaned_data.get('colonia'),
                estado=farmacia_estado,
                municipio=farmacia_municipio,
                cp=form.cleaned_data.get('cp'),
                telefono=form.cleaned_data.get('telefono'),
                email=form.cleaned_data.get('email'),

            )





            new_derechohabiente.save()
            return HttpResponseRedirect('/derechoHabiente/registeredDerechoHabiente/')
    else:
        form = DerechoHabienteForm()

    return render(request, '../templates/registerDerechoHabiente.html', {'Form': form})

@login_required
def RegisterDerechoHabienteGerente(request,idEmpleado):


    if request.method == 'POST':
        form = DerechoHabienteForm(request.POST,request.user)
        if form.is_valid():
            model = Gerente.objects.get(user_id=idEmpleado)

            id_farmacia = model.farmacia_id
            farmacia = Farmacia.objects.get(id = id_farmacia)
            farmacia_estado=farmacia.estado
            farmacia_municipio=farmacia.municipio
            farmacia_cp = farmacia.cp

            new_derechohabiente = DerechoHabiente(
                ficha=form.cleaned_data.get('ficha'),
                codigo = form.cleaned_data.get('codigo'),
                org = form.cleaned_data.get('org'),
                farmacia =farmacia,
                nombre = form.cleaned_data.get('nombre'),
                calle_num = form.cleaned_data.get('calle_num'),
                colonia =form.cleaned_data.get('colonia'),
                estado = farmacia_estado,
                municipio = farmacia_municipio,
                cp = form.cleaned_data.get('cp'),
                telefono = form.cleaned_data.get('telefono'),
                email = form.cleaned_data.get('email'),

            )





            new_derechohabiente.save()
            return HttpResponseRedirect('/derechoHabiente/registeredDerechoHabienteGerente/')
    else:
        form = DerechoHabienteForm()

    return render(request, '../templates/registerDerechoHabienteGerente.html', {'Form': form})











