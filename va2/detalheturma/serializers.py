from rest_framework import serializers
from .models import DetalheTurma

class DetalheTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheTurma
        fields = '__all__'
