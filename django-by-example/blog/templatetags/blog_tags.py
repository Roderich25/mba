from django import template
from ..models import Post
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.publicados.count()


@register.inclusion_tag("blog/post/latest_posts.html")
def show_latest_posts(count=5):
    latest_posts = Post.publicados.order_by('-publicado')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.publicados.filter(comentarios__activo=True).annotate(total_comments=Count('comentarios')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
