from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_login",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_login",
        "type": "password",
        "placeholder": "Enter Password"
    }))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_signup",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_signup",
        "type": "email",
        "placeholder": "Enter Email"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_signup",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input_signup",
        "type": "password",
        "placeholder": "Re-Enter Password"
    }))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

