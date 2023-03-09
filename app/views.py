from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rajesh(request):
    return HttpResponse('<h1>he is my best friend</h1>')
