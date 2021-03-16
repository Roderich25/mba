from django.urls import path
from tienda.views import TiendaView

app_name = 'tienda'

urlpatterns = [
    path('', TiendaView.as_view(), name='tienda'),
]
