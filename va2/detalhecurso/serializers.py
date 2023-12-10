from rest_framework import serializers
from .models import DetalheCurso

class DetalheCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheCurso
        fields = '__all__'
