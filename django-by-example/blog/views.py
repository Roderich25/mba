from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm, ComentarioForm, BuscarForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count


class PostListView(ListView):
    queryset = Post.publicados.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/post_list.html'


def posts_list(request, tag_slug=None):
    object_list = Post.publicados.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             slug=post,
                             estatus='publicado',
                             publicado__year=year,
                             publicado__month=month,
                             publicado__day=day)
    comentarios = post.comentarios.filter(activo=True)
    comentario_nuevo = None
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            comentario_nuevo = comentario_form.save(commit=False)
            comentario_nuevo.post = post
            comentario_nuevo.save()
    else:
        comentario_form = ComentarioForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.publicados.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publicado')[:4]
    return render(request, 'blog/post/detail.html',
                  {'post': post,
                   'comentarios': comentarios,
                   'comentario_nuevo': comentario_nuevo,
                   'comentario_form': comentario_form,
                   'posts_similares': similar_posts,
                   })


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, estatus='publicado')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # ... send email
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f'{cd["nombre"]} ({cd["email"]}) te recomienda leer "{post.titulo}"'
            message = f'Leer "{post.titulo}" en {post_url}\n\nComentarios de {cd["nombre"]}:\n{cd["comentarios"]}'
            send_mail(subject, message, 'admin@myblog.com', [cd['para']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})


def post_search(request):
    form = BuscarForm()
    query = None
    results = []
    if 'palabras' in request.GET:
        form = BuscarForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['palabras']
            search_vector = SearchVector('titulo', weight='A') + SearchVector('contenido', weight='B')
            search_query = SearchQuery(query)
            results = Post.objectos.annotate(
                # search=search_vector,
                # rank=SearchRank(search_vector, search_query)
                # ).filter(rank__gte=0.3).order_by('-rank')
                similarity=TrigramSimilarity('titulo', 'query')
            ).filter(similarity=0.3).order_by('-similarity')
    return render(request,
                  'blog/post/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})
