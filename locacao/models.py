from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Veiculo(models.Model):
    ALUGADO_CHOICES = (
        (True, 'Sim'),
        (False, 'Não'),
    )

    placa = models.CharField('Placa', max_length=20, unique=True)
    combustivelNoTanque = models.IntegerField('Combustivel no Tanque',)
    quilometragem = models.DecimalField('Quilometragem',max_digits=10, decimal_places=2)
    alugado = models.BooleanField('Alugado',default=False, choices=ALUGADO_CHOICES, blank=False, null=False)
    precodiaria = models.DecimalField('Preço da Diaria',max_digits=10, decimal_places=2)
    slug = models.SlugField('Slug', max_length=250)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
        ordering = ['placa']

    def abastecer(self, combustivel):
        pass

    def viajar(self, distacia):
        pass

    def __str__(self):
        return self.placa


class Moto(Veiculo):
    cilindrada = models.IntegerField('Cilindradas')

    class Meta:
        verbose_name = 'Moto'
        verbose_name_plural = 'Motos'
        ordering = ['placa']

    def viajar(self, distacia):
        pass


    def __str__(self):
        return self.placa

class Carro(Veiculo):
    potencia = models.IntegerField('Potencia do Motor')

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['placa']

    def viajar(self, distacia):
        pass


    def __str__(self):
        return self.placa

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length=230)
    numero = models.IntegerField('Número')
    slug = models.SlugField('Slug', max_length=250)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'
        ordering = ['slug']


    def __str__(self):
        return self.slug

class Cliente(models.Model):
    cpf = models.CharField('CPF', max_length=20, unique=True)
    nome = models.CharField('Nome', max_length=200)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, blank=True, null=True)
    valorDivida = models.DecimalField('Valor da Divida', max_digits=10, decimal_places=2)
    slug = models.SlugField('Slug', max_length=250)
    autor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='user_posts')

    def Cliente_equals(self):
        pass

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Locacao(models.Model):
    data_inicial = models.DateField('Data Aluguel', default=timezone.now)
    data_dev = models.DateField('Data develução')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, blank=True, null=True)


    class Meta:
        verbose_name = 'Locação'
        verbose_name_plural = 'Locações'
        ordering = ['data_inicial']
