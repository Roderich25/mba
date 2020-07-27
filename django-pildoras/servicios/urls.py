from django.urls import path
from .views import ServiciosView

app_name = 'servicios'

urlpatterns = [
    path('', ServiciosView.as_view(), name='servicios'),
]
