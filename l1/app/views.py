from django.shortcuts import render
from django.http import  HttpResponse

def index(request):
    return HttpResponse("Здесь что-то будет О_о (какие-то объявления)")