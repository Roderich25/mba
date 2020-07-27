from django.views.generic import ListView

from .models import Servicios


class ServiciosView(ListView):
    model = Servicios
    context_object_name = 'servicios'
    template_name = 'servicios/servicios.html'
