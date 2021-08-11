from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def jan(request):
    return HttpResponse("Learn Python")


def feb(request):
    return HttpResponse('Learn a python Framework')


def mar(request):
    return HttpResponse('Build a huge project on python')


def apr(request):
    return HttpResponse('Deploy it online and make money')


def may(request):
    return HttpResponse('Learn Javascript')


def jun(request):
    return HttpResponse('Learn React JS')


def jul(request):
    return HttpResponse('Build React Projecta')


def aug(request):
    return HttpResponse('Lear React Native')


def sep(request):
    return HttpResponse('Learn PHP')


def oct(request):
    return HttpResponse('Learn Laravel')


def nov(request):
    return HttpResponse('Build a microservice')


def dec(request):
    return HttpResponse('Enjoy!')
