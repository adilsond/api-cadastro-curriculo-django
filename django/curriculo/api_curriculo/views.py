from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .permissions import Proprietario
from .serializers import CadastroCurriculoSerializer
from .models import CadastroCurriculo

class CreateView(generics.ListCreateAPIView):
    """Esta classe define a listagem e criação de dados do currículo pela API."""    
    def get_queryset(self):
        user = self.request.user
        return CadastroCurriculo.objects.filter(usuario=user)
    serializer_class = CadastroCurriculoSerializer
    permission_classes = (permissions.IsAuthenticated, Proprietario)

    def perform_create(self, serializer):
        """Salva os dados no momento em que o currículo é cadastrado."""
        serializer.save(usuario=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Essa classe manipula as resquisições http GET, PUT e DELETE."""

    queryset = CadastroCurriculo.objects.all()
    serializer_class = CadastroCurriculoSerializer
    permission_classes = (permissions.IsAuthenticated, Proprietario)
