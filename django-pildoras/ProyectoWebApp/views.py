from django.views.generic import TemplateView


class MyHomeView(TemplateView):
    template_name = 'ProyectoWebApp/home.html'


class BlogView(TemplateView):
    template_name = 'ProyectoWebApp/blog.html'


class TiendaView(TemplateView):
    template_name = 'ProyectoWebApp/tienda.html'


class ContactoView(TemplateView):
    template_name = 'ProyectoWebApp/contacto.html'


class RequestObjectView(TemplateView):
    template_name = 'ProyectoWebApp/request_object.html'
