"""DMHQuiroz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import RegisterReceta,SuccessRegister,RegisterRecetaGerente,SuccessRegisterGerente,ListEquivalenciaGerente,searchReceta,EditReceta,ListEquivalenciaEdit



urlpatterns = [

    path('<int:idEmpleado>/',RegisterReceta,name="RegisterReceta"),
    path('<int:idEmpleado>/Gerente',RegisterRecetaGerente,name="RegisterRecetaGerente"),
    path('<int:idEmpleado>/<int:folio>/',ListEquivalenciaGerente,name="RegisterEquivalencia"),
    path('editReceta/',searchReceta),
    path('editReceta/<int:idEmpleado>/<str:idReceta>/',EditReceta),
    path('editReceta/<int:idEmpleado>/<int:folio>/EditEquivalencia/',ListEquivalenciaEdit),
    path('registeredReceta/',SuccessRegister,name='SuccessRegister'),
    path('registeredRecetaGerente/',SuccessRegisterGerente,name='SuccessRegisterGerente'),

]
