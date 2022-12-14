from django.urls import path
from .views import *

urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('listarveiculos/', ListarVeiculosListView, name='listarveiculos'),
path('listarpdf/', ListaVeiculosPdf, name='listarpdf'),

]