from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DetalheDisciplina
from .serializers import DetalheDisciplinaSerializer

@api_view(['GET'])
def consultar_detalhe_disciplina(request, codigo_curso, codigo_disciplina):
    try:
        detalhe_disciplina = DetalheDisciplina.objects.get(codigoCurso=codigo_curso, codigoDisciplina=codigo_disciplina)
        serializer = DetalheDisciplinaSerializer(detalhe_disciplina)
        return Response(serializer.data)
    except DetalheDisciplina.DoesNotExist:
        return Response({"message": "Detalhe de Disciplina não encontrado"}, status=404)

@api_view(['POST'])
def incluir_detalhe_disciplina(request):
    serializer = DetalheDisciplinaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
