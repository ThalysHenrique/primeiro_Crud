from django.shortcuts import render, redirect
from .models import Livro

def home(request):
    livros = Livro.objects.all()
    return render(request, 'index.html', {"livros": livros})

def salvar(request):
    nome = request.POST.get('nome')
    Livro.objects.create(nome=nome)
    livros = Livro.objects.all()
    return render(request, 'index.html', {"livros": livros})

def editar(request, id):
    livro = Livro.objects.get(id=id)
    return render(request, 'update.html', {"livro": livro})

def update(request, id):
    nome = request.POST.get('nome')
    livro = Livro.objects.get(id=id)
    livro.nome = nome
    livro.save()
    return redirect(home)

def delete(request, id):
    livro = Livro.objects.get(id=id)
    livro.delete()
    return redirect(home)