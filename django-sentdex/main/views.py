from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from main.models import Tutorial
from .forms import NewUserForm


def homepage(request):
    return render(request=request,
                  template_name="main/home.html",
                  context={"tutorials": Tutorial.objects.all}
                  )


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
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

    form = NewUserForm
    return render(request,
                  'main/register.html',
                  context={"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Successfully logged out.")
    return redirect("main:homepage")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Logged in as {username}.")
                return redirect("main:homepage")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})
