from django.db import models

class DetalheCurso(models.Model):
    codigoCurso = models.CharField(max_length=20)
    codigoTurma = models.CharField(max_length=20)

    def __str__(self):
        return f'Detalhe do Curso - Curso: {self.codigoCurso}, Turma: {self.codigoTurma}'
