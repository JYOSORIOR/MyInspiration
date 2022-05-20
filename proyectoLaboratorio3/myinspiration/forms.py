from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = (
            'username',
            'nombre',
            'apellido',
            'email',
            'password1',
            'password2',
        )

class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
