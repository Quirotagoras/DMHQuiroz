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

from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from .forms import EquivalenciaForm,FindRecetaForm,RecetaFormEdit


def parse(string):
    parsed = string.split()
    value = parsed[0]
    return value

def parseCode(string):
    parsed = string.split()
    value = parsed [1]
    return value



def SuccessRegister(request):
    return render(request,'../templates/successReceta.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successRecetaGerente.html')



def searchReceta(request):
    if request.method == 'POST':
        form =FindRecetaForm(request.POST)

        print(form.is_valid())
        if form.is_valid():
            data =form.data['receta']
            return HttpResponseRedirect('/receta/editReceta/'+str(request.user.pk)+'/'+str(data)+'/')

    else:
        form = FindRecetaForm()

    context={'form':form}
    return render(request,'../templates/findReceta.html',context)



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

    print(receta.equivalencia)
    if request.method == 'POST':
        form=EquivalenciaForm(request.POST)
        if form.is_valid():
            try:
                receta.equivalencia=form.cleaned_data.get('equivalencia')
                print(form.cleaned_data.get('equivalencia'))
                receta.equivalencia_obs=form.cleaned_data.get('equivalencia_obs')
                receta.save()
            except Receta.DoesNotExist:
                raise ValidationError('Receta no existe')

            return HttpResponseRedirect('/receta/registeredReceta/')

    context = {'list':equivalencias,'folio':folio,'medicamento':nombre_medicamento,'cantidad':cantidad}
    return render(request, '../templates/listEquivalencia.html', context)

@login_required
def ListEquivalenciaEdit(request,idEmpleado,folio):

    model = Gerente.objects.get(user_id=idEmpleado)
    id_farmacia = model.farmacia_id
    receta = Receta.objects.get(folio_receta=folio,farmacia=id_farmacia)
    medicamento = receta.cbarras
    cantidad = receta.cantidad
    nombre_medicamento = medicamento.nombre_activo+ " " + medicamento.nombre_comercial
    cbarras=medicamento.cbarras


    equivalencias = Equivalencia.objects.filter(cbarras=cbarras)


    if request.method == 'POST':

        form=EquivalenciaForm(request.POST)
        print("Antes"+str(receta.equivalencia))
        if form.is_valid():
            try:
                receta.equivalencia=form.cleaned_data.get('equivalencia')
                print(form.cleaned_data.get('equivalencia'))
                print("DESPUES"+str(receta.equivalencia))
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
                print("NUR:"+form.cleaned_data.get("nur"))





                new_derechohabiente = Receta(
                    nur = form.cleaned_data.get("nur"),
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
        medicamentos.append(str(medicamento.cbarras)+" "+medicamento.nombre_comercial + ' '+medicamento.presentacion+medicamento.nombre_activo)


    #Pasar a contexto

    context = {'Form':form,'DoctoresAutocomplete':doctores,'DHAutocomplete':derechohabientes,'medicamentoAutcomplete':medicamentos}


    return render(request, '../templates/registerReceta.html', context)


@login_required
def EditReceta(request,idEmpleado,idReceta):
    model = Gerente.objects.get(user_id=idEmpleado)
    username = model.user
    user_id = User.objects.get(username=username)
    id_farmacia = model.farmacia_id
    receta = Receta.objects.get(folio_receta=idReceta)



    equivalenciabefore = receta.has_Equivalencia


    # FORM
    if request.method == 'POST':
        print('entre a post')
        form = RecetaFormEdit(request.POST)

        print(form.errors)

        if form.is_valid():
            print('entre a valid')
            #autocomplete derechohabiente
            ficha = request.POST.get('ficha_derechohabiente')
            parsed_ficha = parse(ficha)
            ficha_id = DerechoHabiente.objects.get(ficha=parsed_ficha)

            #autocomplete medicamento
            medicamento = request.POST.get('cbarras')
            parsed_medicamento = parse(medicamento)
            medicamento_id = Product.objects.get(cbarras=parsed_medicamento)


            receta.status=form.cleaned_data.get("status")
            receta.fecha_expide = form.cleaned_data.get("fecha_expide")
            receta.fecha_recibe = form.cleaned_data.get("fecha_recibe")
            receta.fecha_surte = form.cleaned_data.get("fecha_surte")
            receta.doctor = form.cleaned_data.get("doctor")
            receta.ficha_derechohabiente = ficha_id
            receta.cantidad = form.cleaned_data.get("cantidad")
            receta.cbarras = medicamento_id
            receta.ultimamodif = timezone.now()
            receta.has_Equivalencia = form.cleaned_data.get('has_Equivalencia')

            receta.save()

            print('Q'+str(form.cleaned_data.get('changeEquivalencia')))
            #no tenia equivalencia y despues tuvo equivalencia
            if ((form.cleaned_data.get('has_Equivalencia') == True) and equivalenciabefore==False ):
                return HttpResponseRedirect('EditEquivalencia/')
            #tenia equivalencia, ahora no
            elif((form.cleaned_data.get('has_Equivalencia') == False) and equivalenciabefore==True):
                receta.equivalencia=None
                receta.equivalencia_obs=None
                receta.save()
                return HttpResponseRedirect('/receta/registeredRecetaGerente/')
            #no hay modificacion
            elif ((form.cleaned_data.get('has_Equivalencia') == False) and equivalenciabefore == False):
                return HttpResponseRedirect('/receta/registeredRecetaGerente/')

            #tenia equivalencia y quiere cambiar equivalencia
            elif((form.cleaned_data.get('has_Equivalencia') == True) and equivalenciabefore == True and (form.cleaned_data.get('changeEquivalencia')==True)):
                return HttpResponseRedirect('EditEquivalencia/')

            #tenia equivalencia y no se quiere cambiar equivalencia
            elif ((form.cleaned_data.get('has_Equivalencia') == True) and equivalenciabefore == True and (form.cleaned_data.get('changeEquivalencia') == None)):
                return HttpResponseRedirect('/receta/registeredRecetaGerente/')


        else:
            print('entre a not valid')

    else:
        print("entre")
        form = RecetaFormEdit()

    # END form

    # Info for doctor autocomplete
    tempdoctores = Doctor.objects.filter(farmacia=id_farmacia)
    doctorestemp = tempdoctores.all()
    doctores = []

    # Info DerechoHabientes

    tempDerechoHabientes = DerechoHabiente.objects.filter(farmacia=id_farmacia)
    DerechoHabientetemp = tempDerechoHabientes.all()
    derechohabientes = []

    # Info Medicamento

    Medicamentotemp = Product.objects.all()
    medicamentos = []

    # transformar info
    for doctor in doctorestemp:
        doctores.append("Dr. " + doctor.first_name + " " + doctor.last_name + ' ' + doctor.last_name2)

    for derechohabiente in DerechoHabientetemp:
        derechohabientes.append(str(derechohabiente.ficha) + " " + ", Codigo: " + str(
            derechohabiente.codigo) + ", Nombre : " + derechohabiente.nombre + " " + ", Organismo : " + derechohabiente.org)

    for medicamento in Medicamentotemp:
        medicamentos.append(str(
            medicamento.cbarras) + " " + medicamento.nombre_comercial + ' ' + medicamento.presentacion + medicamento.nombre_activo + ' ')


    #contexto
    folio_receta = receta.folio_receta
    derecho = receta.ficha_derechohabiente.pk
    derechohabiente = DerechoHabiente.objects.get(id=derecho)
    derechotemp = (str(derechohabiente.ficha) + " " + ", Codigo: " + str(
        derechohabiente.codigo) + ", Nombre : " + derechohabiente.nombre + " " + ", Organismo : " + derechohabiente.org)

    fecha_expide = receta.fecha_expide

    medi = receta.cbarras.pk
    medicamento = Product.objects.get(id=medi)
    medicamentostring = (str(
            medicamento.cbarras) + " " + medicamento.nombre_comercial + ' ' + medicamento.presentacion + medicamento.nombre_activo + ' ')
    print(medicamento)

    # Pasar a contexto

    context = {'Form': form, 'DoctoresAutocomplete': doctores, 'DHAutocomplete': derechohabientes,
               'medicamentoAutcomplete': medicamentos,'receta':folio_receta,'objecto_receta':receta,'choicederecho':derechotemp,'choice_medicamento':medicamentostring}

    return render(request, '../templates/editReceta.html', context)


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
                parsed_codigo = parseCode(ficha)
                ficha_id = DerechoHabiente.objects.get(ficha=parsed_ficha, codigo=parsed_codigo)
                print(str(ficha_id))

                medicamento = request.POST.get('cbarras')
                parsed_medicamento = parse(medicamento)

                medicamento_id = Product.objects.get(cbarras=parsed_medicamento)




                new_derechohabiente = Receta(
                    nur = form.cleaned_data.get("nur"),
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
        derechohabientes.append(str(derechohabiente.ficha) + " "+str(derechohabiente.codigo)+" "+", Codigo: "+ str(derechohabiente.codigo) + ", Nombre : " + derechohabiente.nombre + " " + ", Organismo : "+derechohabiente.org)


    for medicamento in Medicamentotemp:
        medicamentos.append(str(medicamento.cbarras)+" "+medicamento.nombre_comercial + ' '+medicamento.presentacion+medicamento.nombre_activo+' ')


    #Pasar a contexto

    context = {'Form':form,'DoctoresAutocomplete':doctores,'DHAutocomplete':derechohabientes,'medicamentoAutcomplete':medicamentos}



    return render(request, '../templates/registerRecetaGerente.html', context)















