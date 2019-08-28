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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('doctor/', include('doctores.urls')),
    path('doctorGerente/', include('doctores.urls')),
    path('products/', include('products.urls')),
    path('productsGerente/', include('products.urls')),
    path('farmacias/', include('farmacia.urls')),
    path('farmaciasGerente/', include('farmacia.urls')),
    path('derechoHabiente/', include('derechohabiente.urls')),
    path('derechoHabienteGerente/', include('derechohabiente.urls')),
    path('receta/', include('receta.urls')),
    path('recetaGerente/', include('receta.urls')),
    path('users/',include('users.urls')),
    path('reporte/',include('reporte.urls')),
    path('reporteGerente/',include('reporte.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()