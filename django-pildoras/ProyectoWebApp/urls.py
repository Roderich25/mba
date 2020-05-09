from django.urls import path
from .views import home, servicios, blog, tienda, contacto

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('servicios/', servicios, name='servicios'),
    path('blog/', blog, name='blog'),
    path('tienda/', tienda, name='tienda'),
    path('contacto/', contacto, name='contacto'),
]
