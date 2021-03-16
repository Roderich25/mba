from django.contrib import admin
from tienda.models import CategoriaProducto, Producto


class CategoriaProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", "actualizacion")


class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha", "actualizacion")


admin.site.register(Producto, ProductoAdmin)
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
