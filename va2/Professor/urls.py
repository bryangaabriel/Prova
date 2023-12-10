from django.urls import path
from .views import consultar_turmas, lancar_nota_aluno, realizar_frequencia

urlpatterns = [
    path('consultar-turmas/<str:registro_professor>/', consultar_turmas, name='consultar_turmas'),
    path('lancar-nota-aluno/', lancar_nota_aluno, name='lancar_nota_aluno'),
    path('realizar-frequencia/', realizar_frequencia, name='realizar_frequencia'),
]
