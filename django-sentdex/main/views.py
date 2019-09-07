from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.models import Tutorial


def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created for {username}.")
            login(request, user)
            messages.info(request, f"You are logged in as {username}.")
            return redirect("main:homepage")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    form = UserCreationForm
    return render(request,
                  'main/register.html',
                  context={"form": form})


