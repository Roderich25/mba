from django.shortcuts import HttpResponse
from django.views.generic import View


class MyHomeView(View):

    def get(self, request, *args, **kargs):
        return HttpResponse("Home Sweet Home")


class ServiciosView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Servicios")


class BlogView(View):

    def get(self, request, *args, **kargs):
        return HttpResponse("Blog")


class TiendaView(View):

    def get(self, request, *args, **kargs):
        return HttpResponse("Tienda")


class ContactoView(View):

    def get(self, request, *args, **kargs):
        return HttpResponse("Contacto")
