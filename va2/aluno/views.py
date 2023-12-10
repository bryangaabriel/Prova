from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Aluno
from .serializers import AlunoSerializer

@api_view(['POST'])
def registrar_aluno(request):
    serializer = AlunoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def consultar_aluno(request, matricula):
    aluno = get_object_or_404(Aluno, matricula=matricula)
    serializer = AlunoSerializer(aluno)
    return Response(serializer.data)

@api_view(['DELETE'])
def excluir_aluno(request, matricula):
    aluno = get_object_or_404(Aluno, matricula=matricula)
    aluno.delete()
    return Response(status=204)

@api_view(['PUT'])
def alterar_matricula(request, matricula):
    aluno = get_object_or_404(Aluno, matricula=matricula)
    serializer = AlunoSerializer(aluno, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)
