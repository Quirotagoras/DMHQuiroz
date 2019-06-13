from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login, logout
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Gerente,Capturista

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

