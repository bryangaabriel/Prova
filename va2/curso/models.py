from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.codigo} - {self.nome}'
