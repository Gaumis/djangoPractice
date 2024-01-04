from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home1(request):
    return HttpResponse("<h1>Hello, Django! This is the home page.</h1>")

def home(request):

    people = [
        {'name':'Gaurav', 'age':28},
        {'name':'Pallavi Kumari', 'age':30},
        {'name':'Ranjana Mishra', 'age':50},
        {'name':'Shree Kant Mishra', 'age':49}
    ]

    text = "Hey Gaurav, when you are thinking of getting a new job"

    return render(request, 'home/index.html', context={'people':people, 'textwa':text, 'page_name':'Home'})

def about(request):
    context = {
        'page_name':'About'
    }
    return render(request, 'home/about.html',context)

def contact(request):
    context = {
        'page_name':'Contact'
    }
    return render(request, 'home/contact.html',context)

def success_page(request):
    return HttpResponse("<h1>Success! This is the success page.</h1>")

