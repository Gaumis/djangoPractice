from django.http import HttpResponse
from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    print("view template")
    if request.method=="POST":
        print("HI, inside post")
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description,
        )
        print(data)

        return redirect('/receipes/')
    
    queryset=receipe.objects.all()
    context = {"receipes":queryset}
    
    return render(request, 'receipes.html', context)

@login_required(login_url="/login/")
def delete_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    
    if request.method=="POST":
        print("hI from update")
        data=request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')

    context = {'receipe':queryset}
    
    return render(request, 'update.html', context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            print(f"{username} user doesn't exists")
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user)
            print("login is done")
            return redirect('/receipes/')


    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        ) # password string can't be directly set to user model, it has to be encrypted.

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

        return redirect('/register/')

    return render(request, 'register.html')

