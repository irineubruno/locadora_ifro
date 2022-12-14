from django.urls import path
from .views import *

urlpatterns = [
path('', IndexView.as_view(), name='index'),
path('listarveiculos/', ListarVeiculosListView.as_view(), name='listarveiculos'),
path('listarpdf/', ListaVeiculosPdf.as_view(), name='listarpdf'),

]