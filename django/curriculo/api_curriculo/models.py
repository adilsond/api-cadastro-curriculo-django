from django.db import models

# Create your models here.
class CadastroCurriculo(models.Model):
    usuario = models.ForeignKey('auth.User', related_name='curriculos',
    on_delete=models.CASCADE)
    nome = models.CharField(max_length=90)
    data_nascimento = models.DateField(null=True)
    endereço = models.CharField(max_length=160, null=True)
    telefone_fixo = models.CharField(max_length=90, null=True)
    celular = models.CharField(max_length=90, null=True)
    email = models.EmailField(null=True, blank=True)
    objetivo = models.CharField(max_length=150, null=True)
    perfil_profissional = models.TextField(null=True)
    FORMACAO = (
       ('NAO_INFORMADO', 'Não Informado'),
       ('POS', 'Pós Graduação'),
       ('SUPERIOR', 'Superior Completo'),
       ('MEDIO', 'Ensino Médio Completo'),
       ('FUNDAMENTAL', 'Ensino Fundamntal Completo'),
       ('SEM_ESTUDO', 'Sem formação escolar'),
      )
    escolaridade = models.CharField(max_length=20, choices=FORMACAO, default='NAO_INFORMADO',)
    graduação = models.TextField(null=True) 
    idiomas = models.TextField(null=True)
    historico_profissional = models.TextField(null=True)
    ultimo_salario = models.CharField(max_length=20, null=True)
    pretensão_salarial = models.CharField(max_length=20, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        """Retorna os dados na forma que é lida por humanos."""
        return "{}".format(self.nome)
