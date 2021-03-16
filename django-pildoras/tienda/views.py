from django.views.generic import ListView
from tienda.models import Producto


class TiendaView(ListView):
    model = Producto
    context_object_name = "productos"
    template_name = 'tienda/tienda.html'
