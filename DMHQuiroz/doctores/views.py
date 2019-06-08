from .forms import DoctorForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Doctor
from django.core.exceptions import ValidationError

def RegisterDoctor(request):


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
                estado=form.cleaned_data.get("estado"),
                municipio=form.cleaned_data.get("municipio"),
                cp=form.cleaned_data.get("cp"),
            )
            if len(new_doctor.rfc) >= 12 and len(new_doctor.rfc) <= 13:
                new_doctor.save()
                return HttpResponseRedirect('/registeredDoctor/')
            else:
                raise ValidationError("rfc tiene que ser menor a 12 caracteres")
    else:
        form = DoctorForm()

    return render(request, '../templates/registerDoctor.html', {'DoctorForm': form})





