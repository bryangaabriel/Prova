from django.urls import path
from .views import listar_detalhes_turma

urlpatterns = [
    path('listar-detalhes-turma/<str:codigo_turma>/', listar_detalhes_turma, name='listar_detalhes_turma'),
]
