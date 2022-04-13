
from django.shortcuts import render
from .forms import SignUpForm

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.is_active = False
            user.save()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})