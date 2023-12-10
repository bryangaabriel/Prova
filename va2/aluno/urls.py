from django.urls import path
from .views import registrar_aluno, consultar_aluno, excluir_aluno, alterar_matricula

urlpatterns = [
    path('registrar-aluno/', registrar_aluno, name='registrar_aluno'),
    path('consultar-aluno/<str:matricula>/', consultar_aluno, name='consultar_aluno'),
    path('excluir-aluno/<str:matricula>/', excluir_aluno, name='excluir_aluno'),
    path('alterar-matricula/<str:matricula>/', alterar_matricula, name='alterar_matricula'),
]
