from django.urls import path
from .views import MyHomeView, TiendaView, RequestObjectView

app_name = 'main'

urlpatterns = [
    path('', MyHomeView.as_view(), name='home'),
    path('tienda/', TiendaView.as_view(), name='tienda'),
    path('request/', RequestObjectView.as_view(), name='request'),
]
