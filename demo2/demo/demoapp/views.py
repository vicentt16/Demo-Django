from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HolaMundo(request):
    return HttpResponse("<h2> Hola Mundo </h2>")

def About(request):
    return HttpResponse("<h5> La página se trata de pura verga </h5>")

def Jolines(request):
    return HttpResponse("<h1>Manda a TOMARLOS POR CULOOOOOOOOO</h1>")

def Pito(request):
    return HttpResponse("Pito que rico")