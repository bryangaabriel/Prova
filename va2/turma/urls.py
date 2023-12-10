from django.urls import path
from .views import listar_turmas, listar_alunos_turma

urlpatterns = [
    path('listar-turmas/', listar_turmas, name='listar_turmas'),
    path('listar-alunos-turma/<str:codigo_turma>/', listar_alunos_turma, name='listar_alunos_turma'),
]
