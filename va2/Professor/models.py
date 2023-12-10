from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=10)
    registro = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
