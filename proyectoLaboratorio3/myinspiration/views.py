from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login

def feed(request):
    print(request.user)
    posts = Post.objects.all()

    context = {'post': posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, None)

        if form.is_valid():
            print("post")
            user = form.save()
            print(user)
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('nombre_usuario')
            user.profile.first_name = form.cleaned_data.get('nombre')
            user.profile.last_name = form.cleaned_data.get('apellido')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = True
            user.save()
            print(user)
        else:
            print(form.errors)
    else:

        form = SignUpForm()
    context = { 'form' : form}
    return render(request,'social/register.html', context)



def profile(request):
    return render(request,'social/profile.html')

def login2(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password, user)
        login(request,user)
        print("usuairo", user)
        return redirect('feed')
    else:
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(request, 'social/login.html', context)

def inspirationCreation(request):
    form = InspirationCreation(request.POST)
    photo_form = forms.PhotoForm()
    if request.method == 'POST':

        context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
        }
        return render(request, 'blog/create_blog_post.html', context=context)
