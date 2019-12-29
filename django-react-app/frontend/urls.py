from django.urls import path
from frontend.views import FrontEndView

urlpatterns = [
    path('', FrontEndView.as_view())
]