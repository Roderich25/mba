from django.urls import path
from .views import BlogView, CategoryView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='blog'),
    path('categoria/<int:category_id>/', CategoryView.as_view(), name='categoria'),
]
