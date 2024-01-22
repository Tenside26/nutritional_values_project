from django.shortcuts import render

def calculator_page(request):

    template = "calculator.html"

    return render(request, template, {})
