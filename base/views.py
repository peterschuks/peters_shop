from django.shortcuts import render
from store.models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def home(request):
    products = Product.objects.all().filter(is_available= True)
    paginator = Paginator(products, per_page=6) # also here
    page = request.GET.get('page',)
    paged_product = paginator.get_page(page)
    context = {
        'products': paged_product
    }
    return render(request, 'base/home.html',context)

# Create your views here.
