from django.shortcuts import render, get_object_or_404, redirect
from .models import Jogador
from .forms import JogadorForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



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

@login_required
def criar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES)
        if form.is_valid():
            jogador = form.save(commit=False)
            jogador.usuario = request.user
            form.save()
            return redirect('lista_jogadores')
    else:
        form = JogadorForm()
    return render(request, 'jogadores/formulario.html', {'form': form})

@login_required
def editar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    
    if jogador.usuario != request.user:
        return redirect('lista_jogadores')
    
    if request.method == 'POST':
        form = JogadorForm(request.POST, request.FILES, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('detalhe_jogador', pk=jogador.pk)
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogadores/formulario.html', {'form': form})

@login_required
def excluir_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    
    if jogador.usuario != request.user:
        return redirect('lista_jogadores')
    
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'jogadores/excluir.html', {'jogador': jogador})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso! Faça login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/cadastro.html', {'form': form})