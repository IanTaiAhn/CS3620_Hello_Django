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
        # The key is how I access it in the template.
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)
#     return HttpResponse(template.render(context, request))
# They both do the same thing but render syntax is cleaner.


def item(request):
    return HttpResponse('Item')

# Works as expected. The name of the function is how I cant control the routing.
# def test(request):
#     return HttpResponse('Testing')
