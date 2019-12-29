from django.urls import path, include
from . import views

urlpatterns = [
    path('profile/28/', views.profile, name='profile28'),
    path('profile/<int:username>', views.profile, name='profile'),
    path('profile/<slug:article_name>', views.article, name='profile'),
    path('profile/', views.profile, name='profile'),
]
