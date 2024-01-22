from django.shortcuts import render
from .forms import UserLoginForm

def login_page(request):

    template = "login.html"
    form = UserLoginForm

    return render(request, template, {"form": form})
