from .forms import formRegisterFarmacia
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Farmacia
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required


def SuccessRegister(request):
    return render(request,'../templates/successFarmacia.html')

@login_required
def RegisterFarmacia(request,idEmpleado):

    if request.method == 'POST':
        form = formRegisterFarmacia(request.POST)
        if form.is_valid():
            new_farmacia = Farmacia(


                cve_admin=form.cleaned_data.get('cve_admin'),
                cve_admin2 = form.cleaned_data.get('cve_admin2'),
                nombre = form.cleaned_data.get('nombre'),
                telefono = form.cleaned_data.get('telefono'),
                calle_num = form.cleaned_data.get('calle_num'),
                estado = form.cleaned_data.get('estado'),
                municipio = form.cleaned_data.get('municipio'),
                cp = form.cleaned_data.get('cp'),

            )


            new_farmacia.save()
            return HttpResponseRedirect('/farmacias/registeredFarmacia/')
    else:
        form = formRegisterFarmacia()

    return render(request, '../templates/registerFarmacia.html', {'Form': form})





