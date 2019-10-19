from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add'),
    path('completed/<todo_id>/', views.todo_completed, name='completed'),
    path('delete_all/', views.delete_all, name='del_all'),
    path('delete_completed/', views.delete_completed, name='del_completed'),
]
