from django.shortcuts import render

def login_page(request):

    template = "login.html"

    return render(request, template, {})
