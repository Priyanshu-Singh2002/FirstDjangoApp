import os
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .util import *
from django.conf import settings

def Send_a_email(request):
    subject = 'Email With Attachment By Sanu Thapa'
    message = 'Hey! In this i am attaching a file with it.'
    recipient_list = ['priyanshuthapa93@gmail.com','djcosty452@gmail.com']
    FILE_PATH = os.path.join(settings.BASE_DIR,'public','media','Mine.jpg')
    try:
        SEND_EMAIL_WITH_FILE(subject,message,recipient_list,FILE_PATH)
    except Exception as e:
        print(e)
    return redirect('/')


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