from django.views.generic import ListView
from blog.models import Post, Categoria
from django.shortcuts import get_object_or_404


class BlogView(ListView):
    model = Post
    context_object_name = 'posts'
    extra_context = {'categorias': Categoria.objects.all()}
    template_name = 'blog/blog.html'


class CategoryView(ListView):
    # pk_url_kwarg = 'category_id'
    context_object_name = 'posts'
    template_name = 'blog/categorias.html'
    queryset = Post.objects.all()
    extra_context = {'categorias': Categoria.objects.all()}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(self.__class__, self).get_context_data(**kwargs)
        cat = get_object_or_404(Categoria, pk=self.kwargs.get('category_id'))
        context['category'] = cat.nombre
        return context

    def get_queryset(self):
        cid = self.kwargs.get('category_id')
        return self.queryset.filter(categorias__id=cid)
