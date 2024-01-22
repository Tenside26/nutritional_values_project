from django.urls import path
from . import views


urlpatterns = [
    path('', views.calculator_page, name="calculator")
]