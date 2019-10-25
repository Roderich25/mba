from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'

    def get_queryset(self):
        return Post.objects.filter(active__exact=True).order_by('-id')


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class BlogCreateView(CreateView):
    model = Post
    fields = ('author', 'title', 'body')
    template_name = 'blog/new_post.html'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/edit_post.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home')
