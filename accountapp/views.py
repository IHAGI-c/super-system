from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    return HttpResponse('! 한 우 림 무 야 호 !')
