from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, ProductoForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django import forms
from django.contrib.auth.models import User


def inicio(request):
	context = {}
	return render(request, 'elarbol/inicio.html', context)




def tienda(request):

	data = {
		'productos':Producto.objects.filter(activo = 1, stock__gt=0)
	}

	return render(request, 'elarbol/tienda.html', data)



def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('inicio')
	else:
		form = UserRegisterForm()
	context = { 'form' : form }
	return render(request, 'elarbol/registro.html', context)


@permission_required('elarbol.add_producto')
def agregar(request):
	data = {
		'form':ProductoForm()
	}
	if request.method == 'POST':
		formulario = ProductoForm(request.POST, files=request.FILES)
		if formulario.is_valid():
			formulario.save()
			data['mensaje'] = "Guardado correctamente"
		else:
			data['mensaje'] = "Error, producto NO agregado"
	return render(request, 'elarbol/agregar.html', data)




@permission_required('elarbol.delete_producto')
def eliminar(request, id):
	producto = Producto.objects.get(id=id)
	producto.delete()

	return redirect(to="tienda")





@permission_required('elarbol.update_producto')
def editar(request, id):

    instancia = Producto.objects.get(id=id)
    form = ProductoForm(instance=instancia)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()



    return render(request, "elarbol/editar.html", {'form': form})

