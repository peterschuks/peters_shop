
from django.shortcuts import get_object_or_404, render
from .models import Product
from category.models import category
from cart.models import Cart_item
from cart.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

def store(request, category_slug = None):
   
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.all().filter(category=categories, is_available= True)
        paginator = Paginator(products, 2) # also here
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available= True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        product_count = products.count()
    context = {
        'products': paged_product,#the intial variable here was products, but bcos of pagination
        #i have t0 introduce paged_product 
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

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-date_added').filter(
                Q(description__icontains=keyword)| Q(name__icontains=keyword))
            product_count = products.count()
    context={
        'products': products,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)
# Create your views here.
