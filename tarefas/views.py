from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogador
from .forms import JogadorForm



# Create your views here.
def index(request):
    return render(request, "index.html")

#def jogadores(request):
    #jogadores = Jogador.objects.all()  
    #return render(request, "jogadores.html", {"jogadores": jogadores})

def sobre(request):
    return render(request, "sobre.html")

def lista_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/lista.html', {'jogadores': jogadores})

def detalhe_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    return render(request, 'jogadores/detalhe.html', {'jogador': jogador})

def criar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = JogadorForm()
    return render(request, 'jogadores/formulario.html', {'form': form})

def editar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('detalhe_jogador', pk=jogador.pk)
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogadores/formulario.html', {'form': form})

def excluir_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'jogadores/excluir.html', {'jogador': jogador})