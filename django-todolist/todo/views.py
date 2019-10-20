from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm, NewTodoForm
from django.views.decorators.http import require_POST


def index(request):
    # form = TodoForm()
    form = NewTodoForm()
    todo_list = Todo.objects.order_by('-id')
    context = {"todo_list": todo_list, "form": form}
    return render(request, 'todo/index.html', context=context)


@require_POST
def add_todo(request):
    # form = TodoForm(request.POST)
    form = NewTodoForm(request.POST)
    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        form.save()
    return redirect('index')


def todo_completed(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')


def delete_completed(request):
    Todo.objects.filter(completed=True).delete()
    return redirect('index')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('index')
