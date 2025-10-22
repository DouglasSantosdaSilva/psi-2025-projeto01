from django.shortcuts import render
from .models import Jogador


# Create your views here.
def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = Jogador.objects.all()  
    return render(request, "jogadores.html", {"jogadores": jogadores})

def sobre(request):
    return render(request, "sobre.html")