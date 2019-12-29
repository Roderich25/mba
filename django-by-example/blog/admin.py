from django.contrib import admin
from . models import Post, Comentario


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'post', 'creado', 'activo')
    list_filter = ('activo', 'creado', 'actualizado')
    search_fields = ('nombre', 'email', 'comentario')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publicado', 'estatus')
    list_filter = ('estatus', 'creado', 'publicado', 'autor')
    search_fields = ('titulo', 'contenido')
    raw_id_fields = ('autor',)
    date_hierarchy = 'publicado'
    ordering = ('estatus', 'publicado')
    prepopulated_fields = {'slug': ('titulo', )}


