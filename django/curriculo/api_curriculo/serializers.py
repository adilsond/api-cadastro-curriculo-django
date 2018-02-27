from rest_framework import serializers
from .models import CadastroCurriculo

class CadastroCurriculoSerializer(serializers.ModelSerializer):
    """Serializer para mapear o modelo para o formato JSON."""
    usuario = serializers.ReadOnlyField(source='usuario.username') 

    class Meta:
        """Meta classe para mapear os campos serializados com os campos do modelo."""
        model = CadastroCurriculo
        fields = ('id', 'usuario',  'nome', 'data_nascimento', 'endereço', 
        'telefone_fixo', 'celular',  'email', 'objetivo',  
        'perfil_profissional' , 'escolaridade', 'graduação', 
        'idiomas', 'historico_profissional', 'ultimo_salario', 
        'pretensão_salarial',  'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
