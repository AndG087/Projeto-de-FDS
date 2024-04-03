from django.db import models

class Empresa (models.Model):
    nome = models.CharField(max_length=50)
    datanasci = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__ (self) -> str:
        return self.nome
