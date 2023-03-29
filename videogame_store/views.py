from rest_framework import viewsets
from .serializer import JogoSerializer
from .models import Jogo
from .serializer import LojaSerializer
from .models import Loja

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer
