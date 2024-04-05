from django.db import models
from django.contrib.auth.models import User

class PersonUser(models.Model):
    imagem = models.URLField()
    descricao = models.CharField(max_length=500)

    def __str__ (self) -> str:
        return self.nome


class Avaliacao(models.Model):
    funcionario_nome = models.CharField(max_length=100)
    nota = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")

    def str(self) -> str:
        return self.title
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    participants = models.CharField(max_length=200)