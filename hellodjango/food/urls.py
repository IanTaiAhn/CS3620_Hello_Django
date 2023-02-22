from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # root is /food/
    path('', views.index, name="index"),
    path('item', views.item, name="item"),
    # The path is what our client side sees, and is the URL
    # The views.<'name'> is how we connect the path to our view which proccess the request, and renders the html.
    # The name parameter is how we can access this path dynamically from our templates/html files.
    path('<int:item_id>', views.detail, name="detail"),
    path('add', views.create_item, name="create_item"),
    path('update/<int:id>', views.update_item, name="update_item"),
    path('delete/<int:id>', views.delete_item, name="delete_item"),
]
