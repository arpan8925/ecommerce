from django.shortcuts import render
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, ProductImages, ProductReview, Wishlist, Address

# Create your views here.

def index(request):
    # product = Product.objects.all().order_by("-id")

    product = Product.objects.filter(product_status = "published", featured = True).order_by("-id")

    context = {
        "products" : product
    }
    return render(request, 'core/index.html', context)
