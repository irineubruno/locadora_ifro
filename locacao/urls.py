from django.urls import path
from .views import *

urlpatterns = [
#path('', IndexView.as_view(), name='index'),
path('', ListarVeiculosListView.as_view(), name='listar'),
path('listarpdf/', ListaVeiculosPdf.as_view(), name='listarpdf'),

]