from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Wow, this is something made without the tutorial :O whaddup")   ##Theory: This gets ignored
                                                                                         ##cause of the one below?

def index(request):
    return HttpResponse("Does this work?")
# Create your views here.
