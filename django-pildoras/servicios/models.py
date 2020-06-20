from django.db import models


class Servicios(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Servicios'


