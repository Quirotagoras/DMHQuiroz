from .forms import DoctorForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Doctor
from django.core.exceptions import ValidationError
from farmacia.models import Farmacia
from users.models import Gerente,Capturista
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def SuccessRegister(request):
    return render(request,'../templates/successDoctor.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successDoctorGerente.html')




def DoctorList (request,idEmpleado):

    model = Gerente.objects.get(user_id=idEmpleado)
    id_farmacia = model.farmacia_id
    doctor_list = Doctor.objects.filter(farmacia=id_farmacia)
    page = request.GET.get('page',1)
    paginator = Paginator(doctor_list,2)
    try:
        doctors = paginator.page(page)
    except PageNotAnInteger:
        doctors = paginator.page(1)
    except EmptyPage:
        doctors = paginator.page(paginator.num_pages)

    return render(request,'../templates/listDoctors.html',{'doctors':doctors})


def editDoctor(request,idEmpleado,idDoctor):
    doctor = Doctor.objects.get(pk=idDoctor)

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor.first_name = form.cleaned_data.get("first_name")
            doctor.last_name =  form.cleaned_data.get("last_name")
            doctor.last_name2 = form.cleaned_data.get("last_name2")
            doctor.cedula = form.cleaned_data.get('cedula')
            doctor.telefono = form.cleaned_data.get("telefono")
            doctor.rfc = form.cleaned_data.get("rfc")
            doctor.calle_num = form.cleaned_data.get('calle_num')
            doctor.cp = form.cleaned_data.get("cp")
            doctor.save()
            return HttpResponseRedirect('/doctor/registeredDoctorGerente/')

    else:
        form = DoctorForm()

    context = {'Form':form, 'doctor':doctor}
    return render(request, '../templates/editDoctor.html',context)



@login_required
def RegisterDoctor(request,idEmpleado):


    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            model = Capturista.objects.get(user_id=idEmpleado)

            id_farmacia = model.farmacia_id
            farmacia = Farmacia.objects.get(id=id_farmacia)
            farmacia_estado = farmacia.estado
            farmacia_municipio = farmacia.municipio

            new_doctor = Doctor(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                last_name2=form.cleaned_data.get("last_name2"),
                cedula=form.cleaned_data.get("cedula"),
                telefono=form.cleaned_data.get("telefono"),
                rfc=form.cleaned_data.get("rfc"),
                calle_num=form.cleaned_data.get("calle_num"),
                farmacia=farmacia,
                estado=farmacia_estado,
                municipio=farmacia_municipio,
                cp=form.cleaned_data.get("cp"),
            )


            new_doctor.save()
            return HttpResponseRedirect('/doctor/registeredDoctor/')
    else:
        form = DoctorForm()

    return render(request, '../templates/registerDoctor.html', {'DoctorForm': form})

@login_required
def RegisterDoctorGerente(request,idEmpleado):

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            model = Gerente.objects.get(user_id=idEmpleado)

            id_farmacia = model.farmacia_id
            farmacia = Farmacia.objects.get(id=id_farmacia)
            farmacia_estado = farmacia.estado
            farmacia_municipio = farmacia.municipio


            new_doctor = Doctor(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                last_name2=form.cleaned_data.get("last_name2"),
                cedula=form.cleaned_data.get("cedula"),
                telefono=form.cleaned_data.get("telefono"),
                rfc=form.cleaned_data.get("rfc"),
                calle_num=form.cleaned_data.get("calle_num"),
                farmacia = farmacia,
                estado = farmacia_estado,
                municipio=farmacia_municipio,
                cp=form.cleaned_data.get("cp"),
            )


            new_doctor.save()
            return HttpResponseRedirect('/doctor/registeredDoctorGerente/')
    else:
        form = DoctorForm()

    return render(request, '../templates/registerDoctorGerente.html', {'DoctorForm': form})




