from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
peoples = [
    {'name':'Alice', 'age':30,'email':'alice@example.com','phone':'123-456-7890'},
    {'name':'Bob', 'age':15,'email':'bob@example.com','phone':'123-456-7890'},
    {'name':'Charlie', 'age':35,'email':'charlie@example.com','phone':'123-456-7890'},
    {'name':'David', 'age':17,'email':'david@example.com','phone':'123-456-7890'},
    {'name':'Eve', 'age':22,'email':'eve@example.com','phone':'123-456-7890'},
    {'name':'Frank', 'age':14,'email':'frank@example.com','phone':'123-456-7890'}
]

def home(request):
    context = {'title': 'home | page'}
    return render(request,'home/index.html')


def about(request):
    context = {'title': 'About | page'}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {'peoples': peoples,'title': 'Contact | page'}
    return render(request, 'home/contact.html',context)