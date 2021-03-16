from django.urls import path
from .views import MyHomeView, RequestObjectView

app_name = 'main'

urlpatterns = [
    path('', MyHomeView.as_view(), name='home'),
    path('request/', RequestObjectView.as_view(), name='request'),
]
