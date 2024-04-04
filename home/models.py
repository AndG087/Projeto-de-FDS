from django.db import models

class PersonUser(models.Model):
    imagem = models.URLField()
    descricao = models.CharField(max_length=500)

    def __str__ (self) -> str:
        return self.nome
  