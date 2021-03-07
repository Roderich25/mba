from django.views.generic import ListView
from blog.models import Post, Categoria


class BlogView(ListView):
    model = Post
    context_object_name = 'posts'
    extra_context = {'categorias': Categoria.objects.all()}
    template_name = 'blog/blog.html'
