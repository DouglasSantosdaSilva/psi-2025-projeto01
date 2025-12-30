from django.db import models
from django.conf import settings

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    posicao = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jogadores/', blank=True, null=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome