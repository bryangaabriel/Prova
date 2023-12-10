from django.urls import path
from .views import listar_detalhes_curso

app_name = 'detalhecurso'  # Adicione esta linha

urlpatterns = [
    path('listar-detalhes-curso/<str:codigo_curso>/', listar_detalhes_curso, name='listar_detalhes_curso'),
    # Adicione outras URLs conforme necessário
]