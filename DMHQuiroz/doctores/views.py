from .forms import DoctorForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Doctor
from django.core.exceptions import ValidationError
from farmacia.models import Farmacia
from django.contrib.auth.decorators import login_required

def SuccessRegister(request):
    return render(request,'../templates/successDoctor.html')

def SuccessRegisterGerente(request):
    return render(request,'../templates/successDoctorGerente.html')

@login_required
def RegisterDoctor(request,idEmpleado):


    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():

            new_doctor = Doctor(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                last_name2=form.cleaned_data.get("last_name2"),
                cedula=form.cleaned_data.get("cedula"),
                telefono=form.cleaned_data.get("telefono"),
                rfc=form.cleaned_data.get("rfc"),
                calle_num=form.cleaned_data.get("calle_num"),
                farmacia = form.cleaned_data.get("farmacia"),
                estado = form.cleaned_data.get("estado"),
                municipio=form.cleaned_data.get("municipio"),
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

            new_doctor = Doctor(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                last_name2=form.cleaned_data.get("last_name2"),
                cedula=form.cleaned_data.get("cedula"),
                telefono=form.cleaned_data.get("telefono"),
                rfc=form.cleaned_data.get("rfc"),
                calle_num=form.cleaned_data.get("calle_num"),
                farmacia = form.cleaned_data.get("farmacia"),
                estado = form.cleaned_data.get("estado"),
                municipio=form.cleaned_data.get("municipio"),
                cp=form.cleaned_data.get("cp"),
            )


            new_doctor.save()
            return HttpResponseRedirect('/doctor/registeredDoctorGerente/')
    else:
        form = DoctorForm()

    return render(request, '../templates/registerDoctorGerente.html', {'DoctorForm': form})




