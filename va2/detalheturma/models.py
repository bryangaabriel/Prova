from django.db import models

class DetalheTurma(models.Model):
    codigoAluno = models.CharField(max_length=20)
    codigoProfessor = models.CharField(max_length=20)
    codigoTurma = models.CharField(max_length=20)

    def __str__(self):
        return f'Detalhe da Turma - Aluno: {self.codigoAluno}, Professor: {self.codigoProfessor}, Turma: {self.codigoTurma}'
