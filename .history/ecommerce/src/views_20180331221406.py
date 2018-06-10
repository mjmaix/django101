from django.http import HttpResponse
from django.shortcuts import render

define home_page(request):
    return HttpResponse("<h1>Hello World</h1>")