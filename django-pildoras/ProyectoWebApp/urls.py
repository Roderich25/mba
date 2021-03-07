from django.urls import path
from .views import MyHomeView, TiendaView, ContactoView, RequestObjectView

app_name = 'main'

urlpatterns = [
    path('', MyHomeView.as_view(), name='home'),
    path('tienda/', TiendaView.as_view(), name='tienda'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('request/', RequestObjectView.as_view(), name='request'),
]
