from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    posicao = models.CharField(max_length=50)
    nascimento = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jogadores/')

    def __str__(self):
        return self.nome