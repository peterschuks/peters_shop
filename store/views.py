
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import category
from cart.models import Cart_item
from cart.views import _cart_id

def store(request, category_slug = None):
   
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available= True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available= True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
        
    }
    
    return render(request, 'store/store.html', context)

def product_detail(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = Cart_item.objects.filter(cart__cart_id=_cart_id(request), product =single_product).exists()
    except Exception as e:
        raise e

    context ={
        'single_product':single_product,
        'in_cart': in_cart
    }
    return render(request, 'store/product_details.html', context)

# Create your views here.
