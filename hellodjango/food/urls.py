from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    # root is /food/
    path('', views.index, name="index"),
    path('item', views.item, name="item"),
    # The name parameter is how we can access this path dynamically
    path('<int:item_id>', views.detail, name="detail"),
    path('add', views.create_item, name="create_item"),
]
