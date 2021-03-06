from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

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


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'jan':
#         challenge_text = 'Learn Python'
#     elif month == 'feb':
#         challenge_text = 'Learn a python Framework'
#     elif month == 'mar':
#         challenge_text = 'Build a huge project on python'
#     elif month == 'apr':
#         challenge_text = 'Deploy it online and make money'
#     elif month == 'may':
#         challenge_text = 'Learn Javascript'
#     elif month == 'jun':
#         challenge_text = 'Learn React JS'
#     elif month == 'jul':
#         challenge_text = 'Build React Projecta'
#     elif month == 'aug':
#         challenge_text = 'Learn React Native'
#     elif month == 'sep':
#         challenge_text = 'Learn PHP'
#     elif month == 'oct':
#         challenge_text = 'Learn Laravel'
#     elif month == 'nov':
#         challenge_text = 'Build a microservice'
#     elif month == 'dec':
#         challenge_text = 'Enjoy!'
#     else:
#         return HttpResponse('Month not found')
    
#     return HttpResponse(challenge_text)


# def monthly_challenge_by_number(request, month):
#     challenge_text = None
#     if month == 1:
#         challenge_text = 'Learn Python'
#     elif month == 2:
#         challenge_text = 'Learn a python Framework'
#     elif month == 3:
#         challenge_text = 'Build a huge project on python'
#     elif month == 4:
#         challenge_text = 'Deploy it online and make money'
#     elif month == 5:
#         challenge_text = 'Learn Javascript'
#     elif month == 6:
#         challenge_text = 'Learn React JS'
#     elif month == 7:
#         challenge_text = 'Build React Projecta'
#     elif month == 8:
#         challenge_text = 'Learn React Native'
#     elif month == 9:
#         challenge_text = 'Learn PHP'
#     elif month == 10:
#         challenge_text = 'Learn Laravel'
#     elif month == 11:
#         challenge_text = 'Build a microservice'
#     elif month == 12:
#         challenge_text = 'Enjoy!'
#     else:
#         return HttpResponse('Month not found')
    
#     return HttpResponse(challenge_text)

monthly_challenges = {
   'jan' : 'Learn Python',
   'feb' : 'Learn a python Framework',
   'mar' : 'Build a huge project on python',
   'apr' : 'Deploy it online and make money',
   'may' : 'Learn Javascript',
   'jun' : 'Learn React JS',
   'jul' : 'Build React Projecta',
   'aug' : 'Learn React Native',
   'sep' : 'Learn PHP',
   'oct' : 'Learn Laravel',
   'nov' : 'Build a microservice',
   'dec' : 'Enjoy!'
}

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
        response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f'<h1>{challenge_text}</h1>'
        return HttpResponse(response_data)
    except :
        return HttpResponseNotFound("<h1>Month not found</h1>")
    

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>invalid month!</h1>')
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) #from urls.py
    return HttpResponseRedirect(redirect_path)