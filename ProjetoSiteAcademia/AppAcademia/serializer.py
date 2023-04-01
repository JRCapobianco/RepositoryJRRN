from rest_framework import serializers
from .models import Aluno, Funcionario 

#Serializers configurados // Configured Serializers.

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'plano', 'frequencia']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cargo',]