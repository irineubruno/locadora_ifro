from django.contrib import admin

from locacao.models import Moto, Carro, Cliente, Locacao, Endereco

@admin.register(Moto)
class MotoAdmin(admin.ModelAdmin):
    list_display = ('placa',)
    prepopulated_fields = {'slug': ('placa',)}


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('placa',)
    prepopulated_fields = {'slug': ('placa',)}

@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('rua',)
    prepopulated_fields = {'slug': ('rua','numero')}

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

@admin.register(Locacao)
class LocacaoAdmin(admin.ModelAdmin):
    list_display = ('data_inicial',)
