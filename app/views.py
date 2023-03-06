from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(request):
    return HttpResponse('i am creating an application')

def me(request):
    return HttpResponse('<marquee><h1>Srujana Thinnava raaa!</h1></marquee>')
    