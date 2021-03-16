from django.views.generic import TemplateView


class MyHomeView(TemplateView):
    template_name = 'ProyectoWebApp/home.html'


class RequestObjectView(TemplateView):
    template_name = 'ProyectoWebApp/request_object.html'
