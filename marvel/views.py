from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def ironman(request):
    return render(request,'ironman.html')

def spiderman(request):
    return render(request,'spiderman.html')

def captain(request):
    return render(request,'captain.html')

def thor(request):
    return render(request,'thor.html')