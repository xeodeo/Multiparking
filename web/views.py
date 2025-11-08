from django.shortcuts import render

def home(request):
    return render(request, 'web/home.html')

def login_view(request):
    # Aquí deberá ir la lógica de autenticación (más adelante)
    return render(request, 'web/login.html')

def register_view(request):
    # Aquí deberá ir la lógica de registro (más adelante)
    return render(request, 'web/register.html')