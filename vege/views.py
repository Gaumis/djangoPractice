from django.http import HttpResponse
from django.shortcuts import render, redirect
from vege.models import *

# Create your views here.

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

def delete_receipe(request, id):
    queryset = receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')
