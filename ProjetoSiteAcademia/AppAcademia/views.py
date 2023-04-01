from rest_framework import viewsets
from .serializer import AlunoSerializer, FuncionarioSerializer
from .models import Aluno, Funcionario

#Viewsets configurados: AlunoViewset & FuncionarioViewset // Configured Viewsets: AlunoViewset & FuncionarioViewset

class AlunoViewset(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class FuncionarioViewset(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer



