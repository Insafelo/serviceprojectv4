from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MechanicRegistrationForm


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('profile')
            else:
                messages.error(request, 'Неверный логин или пароль.')
        else:
            for error in form.errors.values():
                messages.error(request, error[0])

    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = MechanicRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрированы!')
            return redirect('login')

    else:
        form = MechanicRegistrationForm()

    return render(request, 'main/registration.html', {'form': form})