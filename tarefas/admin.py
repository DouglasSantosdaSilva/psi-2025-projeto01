from django.contrib import admin
from .models import Jogador

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'posicao', 'nascimento')
    search_fields = ('nome', 'posicao', 'nascimento')
