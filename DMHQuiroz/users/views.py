from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Gerente,Capturista
from farmacia.models import Farmacia
from django.views.generic import ListView,FormView
from django.contrib.auth.models import  User
from .forms import UserForm,CapturistaForm
from django.contrib.auth.decorators import login_required


@login_required
def EditCapturistaView(request,id):
    if request.method == 'POST':
        form = CapturistaForm(request.POST)
        if form.is_valid():

            capturista = Capturista.objects.get(id=id)
            capturista.nombre = form.cleaned_data.get("nombre")
            capturista.apellidos=form.cleaned_data.get("apellidos")
            capturista.telefono=form.cleaned_data.get("telefono")
            capturista.email=form.cleaned_data.get("email")
            capturista.save()
            return redirect('/users/misEmpleados')

    user_form = CapturistaForm()
    capturista = Capturista.objects.get(id=id)
    context = {'form': user_form,'empleado':capturista}
    return render(request, '../templates/editCapturista.html', context)


@login_required
def UserRegisterView(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('/users/misEmpleados/'+ str(new_user.pk) +'/crearCapturista')
    user_form = UserForm()
    context={'form':user_form}
    return render(request, '../templates/registerUser.html', context)


@login_required
def CapturistaRegisterView(request,id):
    if request.method == 'POST':
        form = CapturistaForm(request.POST)
        if form.is_valid():
            query = Gerente.objects.get(user=request.user.id)

            new_capturista = Capturista(
                nombre=form.cleaned_data.get("nombre"),
                apellidos=form.cleaned_data.get("apellidos"),
                user_id=id,
                telefono=form.cleaned_data.get("telefono"),
                email=form.cleaned_data.get("email"),
                farmacia=query.farmacia,
                is_active=True,
            )

            new_capturista.save()
            return redirect('/users/misEmpleados')
    user_form = CapturistaForm()
    context={'form':user_form}
    return render(request, '../templates/registerCapturista.html', context)








class MyEmpleadosView(ListView):
    template_name = '../templates/myEmpleados_gerente.html'
    context_object_name = 'myempleadosList'

    def get_queryset(self):
        try:
            user_id=self.request.user.pk
            gerente_id = Gerente.objects.get(user_id=user_id)
            farmacia_id=gerente_id.farmacia_id
            self.capturista=Capturista.objects.filter(farmacia_id=farmacia_id,is_active=True)
        except Capturista.DoesNotExist:
            pass
        return self.capturista.all()


@login_required
def Deactivate(request,idCapturista):
        capturista = Capturista.objects.get(pk=idCapturista)
        capturista.is_active=False
        capturista.save()
        user = capturista.user_id
        userObject = User.objects.get(pk=user)
        userObject.is_active=False
        userObject.save()
        return redirect('/users/misEmpleados/')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('/users/login')



def user_login(request):
    if request.method == 'POST':
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(request,username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_superuser:
                    return redirect('/admin/')
                if user.is_active:
                    login(request,user)
                    try:
                        Gerente.objects.get(user_id=request.user.pk)
                        return redirect('/recetaGerente/'+ str(user.pk)+'/Gerente')
                    except Gerente.DoesNotExist:
                        return redirect('/receta/' + str(user.pk))

                else:
                    return HttpResponse('Disabled account')

    else:
        login_form=LoginForm()



    return render(request,'../templates/login.html',{'login_form':login_form})

