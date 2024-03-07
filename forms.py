from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

        help_texts = {k: "" for k in fields}

class LoginForm(ModelForm):

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )
        help_texts = {k:"" for k in fields }

class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': "¿Qué piensas"}), required=True)

    class Meta:
        model = Post
        fields = ['content']

