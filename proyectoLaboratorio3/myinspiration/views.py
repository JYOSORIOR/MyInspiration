from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import SignUpForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render
from django.db.models import Q


def feed(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.all()
    if queryset:
        posts = Post.objects.filter(
            Q(content__icontains = queryset)
        )
    return render(request, 'social/feed.html', { 'posts': posts})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, None)

        if form.is_valid():
            print("post")
            user = form.save()
            print(user)
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            messages.success(request, f'Usuario creado')
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
    return render(request, 'social/profile.html', {'user': user, 'posts': posts})

def post(request):
    current_user= get_object_or_404(User, pk=request.user.pk)
    if request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Post Enviado')
            return redirect('feed')
    else:
        form = PostForm
    return render(request, 'social/post.html', {'form': form })

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
             form.save()
             return redirect('feed')

    return render(request, 'social/post.html', {'form': form})





def login2(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(username, password, user)
        login(request,user)
        print("usuario", user)
        return redirect('feed')
    else:
        form = LoginForm(request.POST)
        context = {'form': form}
        return render(request, 'social/login.html', context)

def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user = current_user, to_user = to_user_id)
    rel.save()
    messages.success(request, f'sigues a {username}')
    return redirect('feed')

def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship.objects.filter(from_user = current_user.id, to_user = to_user_id).get()
    rel.delete()
    messages.success(request, f'ya no sigues a {username}')
    return redirect('feed')

def delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('feed')


