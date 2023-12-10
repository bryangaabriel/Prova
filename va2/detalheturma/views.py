from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DetalheTurma
from .serializers import DetalheTurmaSerializer

@api_view(['GET'])
def listar_detalhes_turma(request, codigo_turma):
    detalhes_turma = DetalheTurma.objects.filter(codigoTurma=codigo_turma)
    serializer = DetalheTurmaSerializer(detalhes_turma, many=True)
    return Response(serializer.data)
