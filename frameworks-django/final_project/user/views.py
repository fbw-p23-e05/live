from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:user_login')
    else:
        form = RegistrationForm()
        
    return render(request, 'registration/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog:post_create')  # Redirect to post list page after successful login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})



def user_logout(request):
    logout(request)
    return redirect('blog:post_list')