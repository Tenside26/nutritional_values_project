from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages

def login_page(request):

    template = "login.html"
    form = UserLoginForm

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
