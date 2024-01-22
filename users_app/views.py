from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def login_page(request):

    template = "login.html"
    form = UserLoginForm

    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("calculator")

    return render(request, template, {"form": form})


def register_page(request):

    template = "register.html"
    form = UserRegisterForm

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect("login")
        else:
            form = UserRegisterForm()

    return render(request, template, {"form": form})
