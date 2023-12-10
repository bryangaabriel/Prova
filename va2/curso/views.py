from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Curso
from .serializers import CursoSerializer

@api_view(['GET'])
def consultar_curso(request, codigo_curso):
    try:
        curso = Curso.objects.get(codigo=codigo_curso)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)
    except Curso.DoesNotExist:
        return Response({"message": "Curso não encontrado"}, status=404)

@api_view(['POST'])
def incluir_curso(request):
    serializer = CursoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
