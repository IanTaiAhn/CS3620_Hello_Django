from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# so views.index does the thing, so the name of the function determines.


def index(request):
    return HttpResponse('Hello World')


def item(request):
    return HttpResponse('Item')

# Works as expected. The name of the function is how I cant control the routing.
# def test(request):
#     return HttpResponse('Testing')
