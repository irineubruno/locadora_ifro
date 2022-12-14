from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from locacao.models import Veiculo

class IndexView(TemplateView):
    template_name = 'index.html'

class ListarVeiculosListView(ListView):
    model = Veiculo
    template_name = 'listarveiculos.html'
    context_object_name = 'veiculos'