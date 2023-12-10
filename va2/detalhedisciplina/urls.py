from django.urls import path
from .views import consultar_detalhe_disciplina, incluir_detalhe_disciplina

urlpatterns = [
    path('consultar-detalhe-disciplina/<str:codigo_curso>/<str:codigo_disciplina>/', consultar_detalhe_disciplina, name='consultar_detalhe_disciplina'),
    path('incluir-detalhe-disciplina/', incluir_detalhe_disciplina, name='incluir_detalhe_disciplina'),
    # Adicione outras URLs conforme necessário
]
