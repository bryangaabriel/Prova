from django.urls import path
from .views import consultar_disciplina, incluir_disciplina

urlpatterns = [
    path('consultar-disciplina/<str:codigo_disciplina>/', consultar_disciplina, name='consultar_disciplina'),
    path('incluir-disciplina/', incluir_disciplina, name='incluir_disciplina'),
    
]
