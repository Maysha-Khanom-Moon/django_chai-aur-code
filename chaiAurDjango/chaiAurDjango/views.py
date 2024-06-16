from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at chai aur Djanog home page")
    return render(request, 'website/index.html')


def about(request):
    return HttpResponse("Hello, world. You are at chai aur Djanog about page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Djanog contact page")