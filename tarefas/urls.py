from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
   # path('jogadores/', views.jogadores, name="jogadores"),
    path('sobre/', views.sobre, name="sobre"),
    path('jogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('jogadores/novo/', views.criar_jogador, name='criar_jogador'),
    path('jogadores/<int:pk>/', views.detalhe_jogador, name='detalhe_jogador'),
    path('jogadores/<int:pk>/editar/', views.editar_jogador, name='editar_jogador'),
    path('jogadores/<int:pk>/excluir/', views.excluir_jogador, name='excluir_jogador'),
]