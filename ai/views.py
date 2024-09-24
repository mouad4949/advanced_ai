from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
# Create your views here.
def index(request):
    return render(request, "theme/base.html")

def BackOffice(request):
    return render(request, "theme/Boff.html")

def login_view_b(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # Enlever `request`
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('ai:index') 
            else:
                # Gérer l'erreur si l'utilisateur ne peut pas être authentifié
                form.add_error(None, "email ou mot de passe incorrect")
    else:
        form = LoginForm()

    return render(request, 'theme/login.html', {'form': form})


def login_view_f(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # Enlever `request`
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('ai:index') 
            else:
                # Gérer l'erreur si l'utilisateur ne peut pas être authentifié
                form.add_error(None, "email ou mot de passe incorrect")
    else:
        form = LoginForm()
    return render(request, 'theme/login_front.html', {'form': form})