from django.urls import path
from . import views


urlpatterns = [
    path('calculator', views.calculator_page, name="calculator")
]