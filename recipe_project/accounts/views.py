from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.decorators.cache import never_cache

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@never_cache
def signup(request):
    if request.user.is_authenticated:
        return redirect('recipe_list')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipe_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@never_cache
def custom_logout(request):
    logout(request)
    # Invalidate the session
    request.session.flush()
    # Clear all cookies
    response = redirect('login')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response