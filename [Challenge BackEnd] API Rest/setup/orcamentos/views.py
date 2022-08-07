from django.http import JsonResponse
from orcamentos.models import Despesas, Receitas
from rest_framework import viewsets
from orcamentos.serializer import DespesasSerializer, ReceitasSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class DespesasViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as despesas'''
    queryset = Despesas.objects.all()
    serializer_class = DespesasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ReceitasViewSet(viewsets.ModelViewSet):
    '''Exibindo todas as despesas'''
    queryset = Receitas.objects.all()
    serializer_class = ReceitasSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]






