from django.shortcuts import render
from django.http  import HttpResponse


def index(request):
    print("hola soy un log de servidor.")
    print("--entrando al index")
    return HttpResponse("hola soy un index")
