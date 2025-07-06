from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores = [
        {"nome":"Matheus Cunha", "idade": "24",
         "posicao": "Goleiro", "nascimento": "Tupi Paulista",
         "foto": "img/mateus-cunha-goleiro.webp"},
        {"nome":"Cleiton santana", "idade": "22",
         "posicao": "Zagueiro", "nascimento": "Taperoá, Bahia",
         "foto": "img/img-cleiton.webp"},
        {"nome":"Guillermo Varela", "idade": "32",
         "posicao": "Lateral direito", "nascimento": "Montevidéu, uruguai",
         "foto": "img/img-varela.webp"},
        {"nome":"Alex Sandro", "idade": "34",
         "posicao": "Lateral esquerdo", "nascimento": "São Paulo",
         "foto": "img/img-alex.webp"},
        {"nome":"Evertton Araújo", "idade": "22",
         "posicao": "Volante", "nascimento": "Volta Redonda",
         "foto": "img/img-evertton-araújo.webp"},      
        {"nome":"Erick Antonio", "idade": "31",
         "posicao": "Volante", "nascimento": "Antofagasta, Chile",
         "foto": "img/img-erick.webp"},   
        {"nome":"Jorge Luiz", "idade": "33",
         "posicao": "Volante", "nascimento": "Imbituba, Santa Catarina",
         "foto": "img/img-jorginho.webp"},
        {"nome":"Matheus Gonçalves", "idade": "19",
         "posicao": "Meias", "nascimento": "Rio de Janeiro",
         "foto": "img/img-matheus-gonçalves.webp"},
        {"nome":"De Arrascaeta", "idade": "31",
         "posicao": "Meias", "nascimento": "Nuevo Berlín",
         "foto": "img/img-arrascaeta.webp"},
        {"nome":"Diego Nicolas", "idade": "28",
         "posicao": "Meias", "nascimento": "Montevidéu, Uruguai",
         "foto": "img/img-delacruz.webp"},
        {"nome":"Michael Richard", "idade": "29",
         "posicao": "Atacante", "nascimento": "Poxoréu, Mato Grosso",
         "foto": "img/img-michael.webp"},
        {"nome":"Everton Sousa", "idade": "29",
         "posicao": "Atacante", "nascimento": "Maracanaú, ceará",
         "foto": "img/img-everton.webp"},
         
    ]
    context = {
        "jogadores": jogadores
    }
    return render(request, "jogadores.html", context)

def sobre(request):
    return render(request, "sobre.html")