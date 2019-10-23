from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView
from blog.models import Post


class MyView(View):

    def get(self, request):
        return HttpResponse("Hello, World!")


class MyTemplateView(TemplateView):
    template_name = 'class_based_views/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = [p.titulo for p in Post.publicados.all()]
        return context


class MyListView(ListView):
    model = Post
    paginate_by = 4
    template_name = 'class_based_views/list.html'


