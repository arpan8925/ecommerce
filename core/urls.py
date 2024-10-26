from django.urls import path
from core.views import *
from core import views

app_name = "core"

urlpatterns = [
    path('', index, name='index'),
    path('products/', product_list_view, name='product-list'),
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>', category_product_list_view, name='category_product_list'),
]