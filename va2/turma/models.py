from django.db import models
from django.utils import timezone

class Turma(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    codigoCurso = models.CharField(max_length=20)

    def __str__(self):
        return self.codigo
