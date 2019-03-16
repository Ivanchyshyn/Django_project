from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    my_context = {}
    return render(request, 'index.html', my_context)


def blog(request, *args, **kwargs):
    my_context = {}
    return render(request, 'blog.html', my_context)


def about(request, *args, **kwargs):
    my_context = {}
    return render(request, 'about.html', my_context)


def contact(request, *args, **kwargs):
    my_context = {}
    return render(request, "contact.html", my_context)