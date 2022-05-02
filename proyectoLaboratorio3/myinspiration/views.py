from django.shortcuts import render, redirect
from .models import *
from .forms import SignUpForm


def feed(request):
    posts = Post.objects.all()

    context = {'post': posts}
    return render(request, 'social/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.username = form.cleaned_data.get('username')
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
    else:
        form = SignUpForm()
    context = { 'form' : form}
    return render(request,'social/register.html', context)



def profile(request):
    return render(request,'social/profile.html')



