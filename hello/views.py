from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"hello/index.html")

def amit(request):
    return HttpResponse("hello,Amit!")

def suraj(request):
    return HttpResponse("hello,suraj")

def greet(request,name):
    return render(request,"hello/greet.html",{
        "pin":name
    })
