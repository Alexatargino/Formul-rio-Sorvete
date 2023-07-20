from django.shortcuts import render, redirect
from .forms import Sorveteforms

def sorvete_pedido(request):
    if request.method == 'post':
        form = Sorveteforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedido')# redireciona para a pagina de sucesso após salvar
    else:
        form = Sorveteforms()
    return render(request, 'main/index.html', {'form':form})