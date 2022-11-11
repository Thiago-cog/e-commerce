from django.shortcuts import render
from django.db import connection

def home(request):
    return render(request, 'home/index.html')

def cadastrar(request):
    return render(request, 'cadastro/cadastro.html')

def login(request):
    return render(request, 'cadastro/login.html')


def inserir(request):

    context = {}

    if request.method == 'POST':

        email = request.POST.get('email', None)
        nome = request.POST.get('nome', None)
        sobrenome = request.POST.get('sobrenome', None)
        password = request.POST.get('password', None)
        
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO app_cliente(nome, sobrenome, email, senha) VALUES(%s, %s, %s, %s)", [nome, sobrenome, email, password])

        context['sucesso'] = True 

    return render(request, 'cadastro/cadastro.html', context=context)

def login(request):

    if request.method == 'POST':
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT true FROM app_cliente WHERE email = %s AND senha = %s", [email, password])
            result = cursor.fetchone()
           
        if result == None:
            result = [False] 
    
        if result[0] == True:
            return render(request, 'home/produtos.html')
        else:
            context = {}
            context['erro'] = True
            return render(request, 'cadastro/login.html', context=context)
    else:
        return render(request, 'cadastro/login.html')