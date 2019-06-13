from .forms import formRegisterProduct
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from equivalencia.models import Equivalencia
from django.core.exceptions import ValidationError
from users.models import Gerente
from django.contrib.auth.decorators import login_required

def SuccessRegister(request):
    return render(request,'../templates/successProducto.html')


@login_required
def RegisterProduct(request,idEmpleado):
    context={}
    if request.method == 'POST':
        form= formRegisterProduct(request.POST)
        if form.is_valid():
            new_product = Product(

                cbarras=form.cleaned_data.get("cbarras"),
                subcuenta = form.cleaned_data.get("subcuenta"),
                nombre_comercial = form.cleaned_data.get("nombre_comercial"),
                nombre_activo = form.cleaned_data.get("nombre_activo"),
                presentacion = form.cleaned_data.get("presentacion"),
                cantidad_pastillas = form.cleaned_data.get("cantidad_pastillas"),
                unidad_medida = form.cleaned_data.get("unidad_medida"),
                precio_max_pub = form.cleaned_data.get("precio_max_pub"),
            )

            new_equivalencia= Equivalencia(
                cbarras=form.cleaned_data.get("cbarras"),
                subcuenta=form.cleaned_data.get("subcuenta"),
                nombre_comercial=form.cleaned_data.get("nombre_comercial"),
                nombre_activo=form.cleaned_data.get("nombre_activo"),
                presentacion=form.cleaned_data.get("presentacion"),
                cantidad_pastillas=form.cleaned_data.get("cantidad_pastillas"),
                unidad_medida=form.cleaned_data.get("unidad_medida"),
                precio_max_pub=form.cleaned_data.get("precio_max_pub"),


            )



            new_product.save()
            new_equivalencia.save()
            return HttpResponseRedirect('/products/registeredProduct/')
    else:
        form = formRegisterProduct()

    try:
        Gerente.objects.get(user_id=request.user.pk)
        context={'form':form}
    except Gerente.DoesNotExist:
        #empleado
        pass






    return render(request, '../templates/registerProduct.html', context)





