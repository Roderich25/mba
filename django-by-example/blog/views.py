from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail


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


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, estatus='publicado')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{ cd["nombre"] } ({ cd["email"] }) te recomienda leer "{post.titulo}"'
            message = f'Leer "{post.titulo}" en {post_url}\n\nComentarios de {cd["nombre"]}:\n{cd["comentarios"]}'
            send_mail(subject, message, 'admin@myblog.com', [cd['para']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
