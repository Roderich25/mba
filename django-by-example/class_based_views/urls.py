from django.urls import path
from . import views

urlpatterns = [
    path('view', views.MyView.as_view(), name='my-view'),
    path('template-view', views.MyTemplateView.as_view(), name='my-template-view'),
    path('list-view', views.MyListView.as_view(), name='my-list-view'),
]
