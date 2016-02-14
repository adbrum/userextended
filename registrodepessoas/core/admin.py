from django.contrib import admin
from registrodepessoas.core.models import Pessoa


class PessoatModelAdmin(admin.ModelAdmin):
    list_display = ('pk', 'cpf', 'rg', 'tipo_pessoa')
    fields = ('cpf', 'rg', 'tipo_pessoa')

    def pk(self, obj):
        return ("%s %s" % (obj.first_name, obj.last_name))

    pk.short_description = 'Name'


admin.site.register(Pessoa, PessoatModelAdmin)
