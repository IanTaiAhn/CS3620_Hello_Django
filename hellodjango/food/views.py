from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from django.template import loader
# Create your views here.

# so views.index does the thing, so the name of the function determines.


def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('Item')

# Works as expected. The name of the function is how I cant control the routing.
# def test(request):
#     return HttpResponse('Testing')
