from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Compromisso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento: ')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #associando usuário ao evento(Chave estrangeira) ondelete cascade é para excluir todos os eventos caso o user seja deletado

    class Meta:
        db_table = 'compromisso'

    def __str__(self):
        return self.titulo
