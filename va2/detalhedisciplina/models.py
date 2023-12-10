from django.db import models

class DetalheDisciplina(models.Model):
    codigoCurso = models.CharField(max_length=20)
    codigoDisciplina = models.CharField(max_length=20)

    def __str__(self):
        return f'Detalhe da Disciplina - Curso: {self.codigoCurso}, Disciplina: {self.codigoDisciplina}'
