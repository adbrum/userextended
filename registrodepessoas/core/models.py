from django.db import models
from django.contrib.auth.models import User


class Pessoa(User):
    cpf = models.IntegerField(null=False, blank=False)
    rg = models.IntegerField(null=False, blank=False)
    tipo_pessoa = models.IntegerField()

    def __str__(self):
        return '%s' % (self.tipo_pessoa)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        # ordering = ['pk']


class Cliente(models.Model):
    pessoa = models.ForeignKey(Pessoa)
    especificacao_cliente = models.CharField(max_length=20, null=False, blank=False)
