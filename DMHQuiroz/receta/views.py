from .forms import RecetaForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Receta
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User
from farmacia.models import Farmacia
from .models import Receta
from derechohabiente.models import DerechoHabiente
from users.models import Gerente,Capturista
from doctores.models import Doctor
from products.models import Product
from equivalencia.models import Equivalencia

from django import forms
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from .forms import EquivalenciaForm


def parse(string):
    parsed = string.split()
    value = parsed[0]
    return value



def SuccessRegister(request):
    return render(request,'../templates/successReceta.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successRecetaGerente.html')




@login_required
def ListEquivalenciaGerente(request,idEmpleado,folio):
    try:

        model = Gerente.objects.get(user_id=idEmpleado)
    except Gerente.DoesNotExist:
        model = Capturista.objects.get(user_id=idEmpleado)
    id_farmacia = model.farmacia_id
    receta = Receta.objects.get(folio_receta=folio,farmacia=id_farmacia)
    medicamento = receta.cbarras
    cantidad = receta.cantidad
    nombre_medicamento = medicamento.nombre_activo+ " " + medicamento.nombre_comercial
    cbarras=medicamento.cbarras


    equivalencias = Equivalencia.objects.filter(cbarras=cbarras)


    if request.method == 'POST':
        form=EquivalenciaForm(request.POST)
        if form.is_valid():
            try:
                receta.equivalencia=form.cleaned_data.get('equivalencia')
                receta.equivalencia_obs=form.cleaned_data.get('equivalencia_obs')
                receta.save()
            except Receta.DoesNotExist:
                raise ValidationError('Receta no existe')

            return HttpResponseRedirect('/receta/registeredReceta/')

    context = {'list':equivalencias,'folio':folio,'medicamento':nombre_medicamento,'cantidad':cantidad}
    return render(request, '../templates/listEquivalencia.html', context)




@login_required
def RegisterReceta(request,idEmpleado):
    model = Capturista.objects.get(user_id=idEmpleado)
    username = model.user
    user_id = User.objects.get(username=username)
    id_farmacia = model.farmacia_id


    #FORM
    if request.method == 'POST':
        print('entre a post')
        form = RecetaForm(request.POST)

        print(form.errors)

        if form.is_valid():
            print('entre a valid')

            try:
                Receta.objects.get(folio_receta=form.cleaned_data.get('folio_receta'),farmacia_id=id_farmacia)# aqui es la validacion de un solo numero de receta por sucursal
                return HttpResponseRedirect('/recetaGerente/'+str(idEmpleado)+'/Gerente')
            except Receta.DoesNotExist:
                ficha = request.POST.get('ficha_derechohabiente')
                parsed_ficha = parse(ficha)
                ficha_id = DerechoHabiente.objects.get(ficha=parsed_ficha)

                medicamento = request.POST.get('cbarras')
                parsed_medicamento = parse(medicamento)
                medicamento_id = Product.objects.get(cbarras=parsed_medicamento)





                new_derechohabiente = Receta(

                    folio_receta=form.cleaned_data.get("folio_receta"),
                    status=form.cleaned_data.get("status"),
                    fecha_expide=form.cleaned_data.get("fecha_expide"),
                    fecha_recibe=form.cleaned_data.get("fecha_recibe"),
                    fecha_surte=form.cleaned_data.get("fecha_surte"),
                    doctor=form.cleaned_data.get("doctor"),
                    ficha_derechohabiente=ficha_id,
                    cantidad=form.cleaned_data.get("cantidad"),
                    cbarras=medicamento_id,
                    farmacia=Farmacia.objects.get(id=id_farmacia),
                    equivalencia=form.cleaned_data.get("equivalencia_cantidad"),
                    equivalencia_obs=form.cleaned_data.get("equivalencia_obs"),
                    creado=timezone.now(),
                    ultimamodif=timezone.now(),
                    empleado = user_id,
                    has_Equivalencia = form.cleaned_data.get('has_Equivalencia'),

                    )
                new_derechohabiente.save()



            if (form.cleaned_data.get('has_Equivalencia')== True):
                return HttpResponseRedirect(form.cleaned_data.get('folio_receta')+"/")

            else:

                return HttpResponseRedirect('/receta/registeredReceta/')

        else:
            print('entre a not valid')

    else:
        print("entre")
        form = RecetaForm()

    #END form

    #Info for doctor autocomplete
    tempdoctores = Doctor.objects.filter(farmacia=id_farmacia)
    doctorestemp = tempdoctores.all()
    doctores=[]

    #Info DerechoHabientes

    tempDerechoHabientes =DerechoHabiente.objects.filter(farmacia=id_farmacia)
    DerechoHabientetemp = tempDerechoHabientes.all()
    derechohabientes=[]

    #Info Medicamento

    Medicamentotemp = Product.objects.all()
    medicamentos = []

    #transformar info
    for doctor in doctorestemp:
        doctores.append("Dr. "+doctor.first_name+" "+doctor.last_name+' '+doctor.last_name2)

    for derechohabiente in DerechoHabientetemp:
        derechohabientes.append(str(derechohabiente.ficha)+ " " +"Codigo :"+ str(derechohabiente.codigo)+ " "+ derechohabiente.nombre +  " "+ derechohabiente.org)


    for medicamento in Medicamentotemp:
        medicamentos.append(str(medicamento.cbarras)+" "+medicamento.nombre_comercial + ' '+medicamento.presentacion+' de '+str(medicamento.cantidad_pastillas)+' '+medicamento.nombre_activo+' ')


    #Pasar a contexto

    context = {'Form':form,'DoctoresAutocomplete':doctores,'DHAutocomplete':derechohabientes,'medicamentoAutcomplete':medicamentos}


    return render(request, '../templates/registerReceta.html', context)



@login_required
def RegisterRecetaGerente(request,idEmpleado):
    model = Gerente.objects.get(user_id=idEmpleado)
    username = model.user
    user_id = User.objects.get(username=username)
    id_farmacia = model.farmacia_id

    #FORM
    if request.method == 'POST':
        print('entre a post')
        form = RecetaForm(request.POST)

        print(form.errors)

        if form.is_valid():
            print('entre a valid')

            try:
                Receta.objects.get(folio_receta=form.cleaned_data.get('folio_receta'),farmacia_id=id_farmacia)# aqui es la validacion de un solo numero de receta por sucursal
                return HttpResponseRedirect('/recetaGerente/'+str(idEmpleado)+'/Gerente')
            except Receta.DoesNotExist:
                ficha = request.POST.get('ficha_derechohabiente')
                parsed_ficha = parse(ficha)
                ficha_id = DerechoHabiente.objects.get(ficha=parsed_ficha)

                medicamento = request.POST.get('cbarras')
                parsed_medicamento = parse(medicamento)
                medicamento_id = Product.objects.get(cbarras=parsed_medicamento)





                new_derechohabiente = Receta(

                    folio_receta=form.cleaned_data.get("folio_receta"),
                    status=form.cleaned_data.get("status"),
                    fecha_expide=form.cleaned_data.get("fecha_expide"),
                    fecha_recibe=form.cleaned_data.get("fecha_recibe"),
                    fecha_surte=form.cleaned_data.get("fecha_surte"),
                    doctor=form.cleaned_data.get("doctor"),
                    ficha_derechohabiente=ficha_id,
                    cantidad=form.cleaned_data.get("cantidad"),
                    cbarras=medicamento_id,
                    farmacia=Farmacia.objects.get(id=id_farmacia),
                    equivalencia=form.cleaned_data.get("equivalencia_cantidad"),
                    equivalencia_obs=form.cleaned_data.get("equivalencia_obs"),
                    creado=timezone.now(),
                    ultimamodif=timezone.now(),
                    empleado = user_id,
                    has_Equivalencia = form.cleaned_data.get('has_Equivalencia'),

                    )
                new_derechohabiente.save()



            if (form.cleaned_data.get('has_Equivalencia')== True):
                return HttpResponseRedirect(form.cleaned_data.get('folio_receta')+"/")

            else:

                return HttpResponseRedirect('/receta/registeredRecetaGerente/')

        else:
            print('entre a not valid')

    else:
        print("entre")
        form = RecetaForm()

    #END form

    #Info for doctor autocomplete
    tempdoctores = Doctor.objects.filter(farmacia=id_farmacia)
    doctorestemp = tempdoctores.all()
    doctores=[]

    #Info DerechoHabientes

    tempDerechoHabientes =DerechoHabiente.objects.filter(farmacia=id_farmacia)
    DerechoHabientetemp = tempDerechoHabientes.all()
    derechohabientes=[]

    #Info Medicamento

    Medicamentotemp = Product.objects.all()
    medicamentos = []

    #transformar info
    for doctor in doctorestemp:
        doctores.append("Dr. "+doctor.first_name+" "+doctor.last_name+' '+doctor.last_name2)

    for derechohabiente in DerechoHabientetemp:
        derechohabientes.append(str(derechohabiente.ficha) + " " +", Codigo: "+ str(derechohabiente.codigo) + ", Nombre : " + derechohabiente.nombre + " " + ", Organismo : "+derechohabiente.org)


    for medicamento in Medicamentotemp:
        medicamentos.append(str(medicamento.cbarras)+" "+medicamento.nombre_comercial + ' '+medicamento.presentacion+medicamento.nombre_activo+' ')


    #Pasar a contexto

    context = {'Form':form,'DoctoresAutocomplete':doctores,'DHAutocomplete':derechohabientes,'medicamentoAutcomplete':medicamentos}



    return render(request, '../templates/registerRecetaGerente.html', context)















