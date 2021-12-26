from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index2(request):
    return HttpResponse("Hello world! Это мой второй проект в Django")
