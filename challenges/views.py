from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# def jan(request):
#     return HttpResponse("Learn Python")


# def feb(request):
#     return HttpResponse('Learn a python Framework')


# def mar(request):
#     return HttpResponse('Build a huge project on python')


# def apr(request):
#     return HttpResponse('Deploy it online and make money')


# def may(request):
#     return HttpResponse('Learn Javascript')


# def jun(request):
#     return HttpResponse('Learn React JS')


# def jul(request):
#     return HttpResponse('Build React Projecta')


# def aug(request):
#     return HttpResponse('Lear React Native')


# def sep(request):
#     return HttpResponse('Learn PHP')


# def oct(request):
#     return HttpResponse('Learn Laravel')


# def nov(request):
#     return HttpResponse('Build a microservice')


# def dec(request):
#     return HttpResponse('Enjoy!')


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'jan':
        challenge_text = 'Learn Python'
    elif month == 'feb':
        challenge_text = 'Learn a python Framework'
    elif month == 'mar':
        challenge_text = 'Build a huge project on python'
    elif month == 'apr':
        challenge_text = 'Deploy it online and make money'
    elif month == 'may':
        challenge_text = 'Learn Javascript'
    elif month == 'jun':
        challenge_text = 'Learn React JS'
    elif month == 'jul':
        challenge_text = 'Build React Projecta'
    elif month == 'aug':
        challenge_text = 'Learn React Native'
    elif month == 'sep':
        challenge_text = 'Learn PHP'
    elif month == 'oct':
        challenge_text = 'Learn Laravel'
    elif month == 'nov':
        challenge_text = 'Build a microservice'
    elif month == 'dec':
        challenge_text = 'Enjoy!'
    else:
        return HttpResponse('Month not found')
    
    return HttpResponse(challenge_text)