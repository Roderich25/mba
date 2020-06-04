from django.http import HttpResponse


def index(requets):
    return HttpResponse("Hello world. You're at the polls index.")
