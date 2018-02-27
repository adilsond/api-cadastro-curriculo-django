from rest_framework.permissions import BasePermission
from .models import CadastroCurriculo

class Proprietario(BasePermission):
    """Classe onde permite que o proprietário consiga editar o currículo que cadastrou."""

    def has_object_permission(self, request, view, obj):
        """Retorna true se a autenticação for um sucesso."""
        if isinstance(obj, CadastroCurriculo):
            return obj.usuario == request.user
        return obj.usuario == request.user
