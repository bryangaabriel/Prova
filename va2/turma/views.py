from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Turma
from .serializers import TurmaSerializer

@api_view(['GET'])
def listar_turmas(request):
    turmas = Turma.objects.all()
    serializer = TurmaSerializer(turmas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listar_alunos_turma(request, codigo_turma):
    try:
        turma = Turma.objects.get(codigo=codigo_turma)
    except Turma.DoesNotExist:
        return Response({'detail': 'Turma não encontrada.'}, status=404)


