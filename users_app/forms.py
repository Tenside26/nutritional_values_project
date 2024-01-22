from django import forms
from django.contrib.auth import authenticate


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