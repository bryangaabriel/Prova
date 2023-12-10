from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Disciplina
from .serializers import DisciplinaSerializer

@api_view(['GET'])
def consultar_disciplina(request, codigo_disciplina):
    try:
        disciplina = Disciplina.objects.get(codigo=codigo_disciplina)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)
    except Disciplina.DoesNotExist:
        return Response({"message": "Disciplina não encontrada"}, status=404)

@api_view(['POST'])
def incluir_disciplina(request):
    serializer = DisciplinaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
