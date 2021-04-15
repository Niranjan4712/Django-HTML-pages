from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>Hello from django</h1>')
def contact(request):
    return HttpResponse('<h1>Hello my conatct number is </h1>')
def about(request):
    return HttpResponse('<h1>Hello this is about page </h1>')
def myplace(request):
    return HttpResponse('<h1>Hello this is my place</h1>')
