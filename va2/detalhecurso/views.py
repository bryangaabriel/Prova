from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DetalheCurso
from .serializers import DetalheCursoSerializer

@api_view(['GET'])
def listar_detalhes_curso(request, codigo_curso):
    detalhes_curso = DetalheCurso.objects.filter(codigoCurso=codigo_curso)
    serializer = DetalheCursoSerializer(detalhes_curso, many=True)
    return Response(serializer.data)
