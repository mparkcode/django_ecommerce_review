
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, HttpResponse
from .forms import SignUpForm, ProfileForm

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'registration/signup.html', {'user_form': user_form, "profile_form" : profile_form})

def show_profile(request):
    return render(request, "accounts/profile.html")