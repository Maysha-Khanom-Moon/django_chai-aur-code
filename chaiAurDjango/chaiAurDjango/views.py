from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You are at chai aur Djanog home page")


def about(request):
    return HttpResponse("Hello, world. You are at chai aur Djanog about page")

def contact(request):
    return HttpResponse("Hello, world. You are at chai aur Djanog contact page")