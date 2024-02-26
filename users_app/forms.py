from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        User = get_user_model()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            self.add_error('password1', "Passwords do not match")
            del cleaned_data['password1']

        return cleaned_data

