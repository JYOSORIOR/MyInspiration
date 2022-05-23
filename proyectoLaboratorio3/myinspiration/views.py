from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def feed(request):
    print(request.user)
    posts = Post.objects.all()

    context = {'posts': posts}
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



def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'social/profile.html', {'user':user, 'posts':posts})

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

def seguir(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    segu = Seguidos(from_user = current_user, to_user = to_user_id)
    segu.save()
    messages.success(request, f'sigues a {username}')
    return redirect('home')

def dejardeSeguir(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    segu = Seguidos.objects.filter(from_user = current_user.id, to_user = to_user_id).get()
    segu.delete()
    messages.success(request, f'ya no sigues a {username}')
    return redirect('home')
