from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    return HttpResponse("Hello world")