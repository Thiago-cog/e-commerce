from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    email = models.EmailField()
    senha  = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    nome = models.CharField(max_length=30)
    preco = models.FloatField()
    quantidade = models.BigIntegerField()
    imagem = models.CharField(max_length=300)

    def __str__(self):
        return self.nome