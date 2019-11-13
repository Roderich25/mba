from django.contrib import admin
from .models import Clientes, Pedidos, Articulos

admin.site.register(Clientes)
admin.site.register(Pedidos)
admin.site.register(Articulos)