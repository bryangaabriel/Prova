from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Professor
from .serializers import ProfessorSerializer

@api_view(['GET'])
def consultar_turmas(request, registro_professor):
    try:
        professor = Professor.objects.get(registro=registro_professor)
    except Professor.DoesNotExist:
        return Response({'detail': 'Professor não encontrado.'}, status=404)


@api_view(['POST'])
def lancar_nota_aluno(request):
    # Implemente a lógica para lançar a nota do aluno
    return Response({'detail': 'Lançamento de nota implementado.'}, status=200)

@api_view(['POST'])
def realizar_frequencia(request):
    # Implemente a lógica para realizar a frequência
    return Response({'detail': 'Realização de frequência implementada.'}, status=200)
