from django.urls import path
from .views import MyHomeView, ServiciosView, BlogView, TiendaView, ContactoView

app_name = 'main'

urlpatterns = [
    path('', MyHomeView.as_view(), name='home'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('tienda/', TiendaView.as_view(), name='tienda'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
]
