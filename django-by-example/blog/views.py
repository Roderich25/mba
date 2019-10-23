from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    queryset = Post.publicados.all()
    context_object_name = 'posts'
    paginate_by = 1
    template_name = 'blog/post/post_list.html'


def posts_list(request):
    object_list = Post.publicados.all()
    paginator = Paginator(object_list, 1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             estatus='publicado',
                             publicado__year=year,
                             publicado__month=month,
                             publicado__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})