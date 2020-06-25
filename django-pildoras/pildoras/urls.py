from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWebApp.urls', namespace='main')),
    path('progress/', include('progress.urls', namespace='progress')),
    path('celery-progress/', include('celery_progress.urls')),
]
