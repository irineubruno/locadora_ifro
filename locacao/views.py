from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from locacao.models import Veiculo
from locacao.utils import GeraPDFMixin


class IndexView(TemplateView):
    template_name = 'index.html'

class ListarVeiculosListView(ListView):
    model = Veiculo
    template_name = 'listarveiculos.html'
    queryset = Veiculo.objects.all()
    context_object_name = 'veiculos'

class ListaVeiculosPdf(View, GeraPDFMixin):
    def get(self, request, *args, **kwargs):
        funcs = Veiculo
        context = {
            'veiculos': funcs,
            'quant': funcs.count()
        }
        return self.render_to_pdf('listarpdf.html', context)