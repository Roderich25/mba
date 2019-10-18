from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm


def index(request):
    comments = Comment.objects.order_by('-date_added')
    return render(request, 'guestbook/index.html', context={'comments': comments})


def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(name=request.POST['name'], comment=request.POST['comment'])
            new_comment.save()
            return redirect('index')
    form = CommentForm()
    return render(request, 'guestbook/sign.html', context={'form': form})
