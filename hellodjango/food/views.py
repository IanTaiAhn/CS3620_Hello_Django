from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
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
#   return HttpResponse(template.render(context, request))
# They both do the same thing but render syntax is cleaner.

# TODO Delete


def item(request):
    return HttpResponse('Item')
# Works as expected. The name of the function is how I cant control the routing.
# def test(request):
#     return HttpResponse('Testing')


def detail(request, item_id):
    # item_id is like a get variable in the url
    # We get from our database the item we want according to the url get variable~item_id
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)


def create_item(request):
    # We take the user request and either create a form, or create a none form.
    form = ItemForm(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form})

# The id parameter here is associated with the id in our path url.


def update_item(request, id):
    # We get the item that the request id is equal to in our ddatabase.
    # What is the difference between pk or id?
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request, 'food/item-form.html', {'form': form, 'item': item})
