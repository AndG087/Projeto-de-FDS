from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User



class Avaliacao(models.Model):
    funcionario_nome = models.CharField(max_length=100)
    nota = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Projeto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.CharField(max_length=200)

    def __str__ (self) -> str:
        return self.nome
    
class person(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")
    descricao = models.CharField(max_length=500)

    def str(self) -> str:
        return self.title