from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def home_view(request):
    return render(request, 'index.html')

def page1(request):
    return HttpResponse("<h1>This is page1</h1><p>Go to <a href='/'>home</a></p>")