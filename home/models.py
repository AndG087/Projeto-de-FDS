from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User



class Avaliacao3(models.Model):
    avaliador = models.CharField(max_length=150)  # Campo para armazenar o nome do usuário que fez a avaliação
    avaliado = models.CharField(max_length=100)
    nota = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



class Projeto(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    participants = models.CharField(max_length=255)
    start_date = models.DateField(null=True, blank=True)  # Permite nulos e em branco
    end_date = models.DateField(null=True, blank=True)    # Permite nulos e em branco
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Foto(models.Model):
    arq = models.URLField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def str(self) -> str:
        return self.nome
    
class Descricao(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def str(self) -> str:
        return self.nome
    
#OLA
class Feedback3(models.Model):
    email = models.CharField(max_length=150)
    texto = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)  # Apenas data de criação

    def __str__(self):
        return f"Feedback by {self.user.username} on {self.created_at}"
    
class Anotações(models.Model):
    titulo = models.CharField(max_length=200)
    anotar = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    def str(self) -> str:
        return self.nome
