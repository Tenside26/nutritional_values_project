from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import LoginSerializer


class LoginAPIView(ObtainAuthToken, APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key})


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
