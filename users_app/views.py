from django.shortcuts import render
from .forms import UserLoginForm, UserRegisterForm

def login_page(request):

    template = "login.html"
    form = UserLoginForm

    return render(request, template, {"form": form})

def register_page(request):

    template = "register.html"
    form = UserRegisterForm

    return render(request, template, {"form": form})
