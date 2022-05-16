from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    nombre_usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = (
            'nombre_usuario',
            'nombre',
            'apellido',
            'email',
            'password1',
            'password2',
        )