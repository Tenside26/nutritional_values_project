from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, User


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40, label="Username", widget=forms.TextInput)
    password = forms.CharField(max_length=40, label="Password", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username does not exists")
            if not user.check_password(password):
                raise forms.ValidationError("Wrong Password")


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "first_name", "last_name", "email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already in use")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
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