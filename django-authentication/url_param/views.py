from django.http import HttpResponse


def profile(request, username=''):
    return HttpResponse(f"<h2>Profile page</h2>\n{username}")


def article(request, article_name=''):
    return HttpResponse(f"<p>The article is \n{article_name}.</p>")