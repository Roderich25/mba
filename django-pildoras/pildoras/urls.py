from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWebApp.urls', namespace='main')),
    path('servicios/', include('servicios.urls', namespace='servicios')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('contacto/', include('contacto.urls', namespace='contacto')),
    path('tienda/', include('tienda.urls', namespace='tienda')),
    path('progress/', include('progress.urls', namespace='progress')),
    path('celery-progress/', include('celery_progress.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
