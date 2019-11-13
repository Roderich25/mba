from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post


class LatestPostsFeed(Feed):
    title = 'Mi blog'
    link = '/blog/'
    description = 'Nuevo post en mi blog'

    def items(self):
        return Post.publicados.all()[:5]

    def item_title(self, item):
        return item.titulo

    def item_description(self, item):
        return truncatewords(item.contenido, 30)

