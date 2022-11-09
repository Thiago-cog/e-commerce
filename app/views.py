from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def cadastrar(request):
    return render(request, 'cadastro/cadastro.html')

def inserir(request):
    return render(request, 'home/index.html')