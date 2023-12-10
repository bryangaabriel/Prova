from rest_framework import serializers
from .models import DetalheDisciplina

class DetalheDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheDisciplina
        fields = '__all__'
