from django.views.generic import TemplateView, ListView
from servicios.models import Servicios


class MyHomeView(TemplateView):
    template_name = 'ProyectoWebApp/home.html'


class ServiciosView(ListView):
    model = Servicios
    context_object_name = 'servicios'
    template_name = 'ProyectoWebApp/servicios.html'


class BlogView(TemplateView):
    template_name = 'ProyectoWebApp/blog.html'


class TiendaView(TemplateView):
    template_name = 'ProyectoWebApp/tienda.html'


class ContactoView(TemplateView):
    template_name = 'ProyectoWebApp/contacto.html'


class RequestObjectView(TemplateView):
    template_name = 'ProyectoWebApp/request_object.html'
