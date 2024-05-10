from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import update_session_auth_hash
from .forms import UserEditForm, CustomUserCreationForm
from django.contrib.auth import logout

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': CustomUserCreationForm
        })
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': form,
                    'error': 'Username already exists'
                })
        else:
            return render(request, 'signup.html', {
                'form': form,
                'error': 'Please correct the error below'
            })
        
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        elif hasattr(user, 'profile') and user.profile.is_banned:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Tu cuenta ha sido suspendida. Por favor, contacta al soporte para más información.'
            })
        else:
            login(request, user)
            return redirect('home')
        
def signout(request):
    logout(request)
    return redirect('home')
        
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data['password']
            if new_password:
                user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = UserEditForm(instance=request.user)

    return render(request, 'edit_profile.html', {'form': form})