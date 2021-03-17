from django.db import models


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=60)
    fecha = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría Producto'
        verbose_name_plural = 'Categorías Producto'

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=200)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    disponibilidad = models.BooleanField(default=True)
    fecha = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
