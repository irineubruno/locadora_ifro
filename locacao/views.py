from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from locacao.models import Cliente

class IndexView(TemplateView):
    template_name = 'index.html'

class ListarClientesListView(ListView):
    model = Cliente
    template_name = ''
    context_object_name = 'clientes'