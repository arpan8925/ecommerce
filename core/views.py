from django.shortcuts import render
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address

# Create your views here.

def index(request):
    categories = Category.objects.all()
    product = Product.objects.filter(product_status = "published", featured = True).order_by("-id")
    context = {
        "products" : product,
        "categories": categories
    }
    return render(request, 'core/index.html', context)


def product_list_view(request):
    products = Product.objects.filter(product_status = "published")

    context = {
        "products" : products
    }

    return render(request, 'core/product-list.html', context)


def category_list_view(request):
    categories = Category.objects.all()

    context = {
        "categories": categories
    }
    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status = "published", category = category)

    context = {
        "category": category,
        "products": products,
    }

    return render(request, 'core/category-product-list.html', context)