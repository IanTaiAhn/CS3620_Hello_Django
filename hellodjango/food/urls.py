from . import views
from django.urls import path

# root is /food/
app_name = 'food'
urlpatterns = [
    # path('', views.index, name="index"), # these two index urls are the same, but this one is a fucntion based view.
    # this is a class based view.
    path('', views.IndexClassView.as_view(), name="index"),
    path('item/', views.item, name="item"),
    # path('<int:item_id>', views.detail, name="detail"), #detail function based view
    # detail class based view.
    path('<int:pk>', views.FoodDetail.as_view(), name="detail"),
    # path('add', views.create_item, name="create_item"), # function based
    path('add', views.CreateItem.as_view(), name="create_item"),  # class based
    path('update/<int:id>', views.update_item, name="update_item"),
    path('delete/<int:id>', views.delete_item, name="delete_item"),
]

# The path is what our client side sees, and is the URL
# The views.<'name'> is how we connect the path to our view which proccess the request, and renders the html.
# The name parameter is how we can access this path dynamically from our templates/html files.
