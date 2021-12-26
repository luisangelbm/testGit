from django.shortcuts import render     #render para renderizar plantillas html
from django.http import HttpResponse

# Create your views here.
def hola(request):
    return render(request, 'hola/index.html')

def vader(request):
    return HttpResponse("Hola dark vader!")

def starwars(request):
    return HttpResponse("Star Wars!")

def saludo(request, nombre):
    context = {'name': nombre}
    return render(request, 'hola/saludo.html', context)

def moneda(request):
    num=1
    context = {'num': num}
    return render(request, 'hola/moneda.html', context)