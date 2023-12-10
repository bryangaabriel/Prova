from django.urls import path
from .views import consultar_curso, incluir_curso

urlpatterns = [
    path('consultar-curso/<str:codigo_curso>/', consultar_curso, name='consultar_curso'),
    path('incluir-curso/', incluir_curso, name='incluir_curso'),
]
