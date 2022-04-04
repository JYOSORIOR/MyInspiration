from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse("Hola mundo. Estas en el index de inspirations")


