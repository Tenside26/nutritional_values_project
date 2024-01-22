from django.urls import path
from .view import calculator_page



urlpatterns = [
    path('calculator', views.calculator_page, name="calculator")
]