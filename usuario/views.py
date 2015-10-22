from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from usuario.models import Usuario, criaUsuario

def index(request):
    if request.method == 'POST':
        form = criaUsuario(request.POST)


        if form.is_valid():

            form.save()
            return HttpResponseRedirect('/')

    else:
        form = criaUsuario()

    return render(request, 'inicio/cadastrar.html',{'formulario': form})