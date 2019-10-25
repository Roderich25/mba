from django.contrib import admin
from .models import Post
from tinymce.widgets import TinyMCE
from django.db import models


# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'active')