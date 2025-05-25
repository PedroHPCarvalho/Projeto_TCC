from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')  # redireciona para a rota 'login' se não estiver autenticado
def home(request):
    return render(request, "gest_financeira/home.html")
