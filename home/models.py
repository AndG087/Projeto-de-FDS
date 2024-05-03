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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_ (self) -> str:
        return self.nome
    
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