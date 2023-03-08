
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from .models import Cart, Cart_item

# here i create my add to cart function, what this function does is to get the product by
# the product id and add it to the cart , so firstly, i get the product, filter the product by 
# id and save it in a variable. then set up a try and except block, to get the cart, so that 
# if there is no cart , i can create one on the except block. and to get the cart, is also by
# cart id, and the cart id i created as cookies directly from the web page to the database
# so i can get it using a session key or session id directly from the web . therefore, i have
# to create another fuction to help me easily get this session id.
# the codes below are easily explained as i was able to understand everything happening. 

# this functions gets cart id from the web and pass it to those functions below for use.
def _cart_id(request):
    cart= request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

# this function adds a product to the cart and no mater how many times you add the product, it
# keeps increasing the quantity of the product a customer wants. 
def add_to_cart(reguest, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(reguest))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id= _cart_id(reguest))
    cart.save()
    try:
        cart_item = Cart_item.objects.get(product = product, cart= cart)
        cart_item.quantity  += 1
        cart_item.save()
    except Cart_item.DoesNotExist:
        cart_item = Cart_item.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
    cart_item.save()

    return redirect('cart')
# this function deletes and reduce the quantity of product in cart item. when the quantity is now
# equal to zero, it deletes the cart_item. 
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id= product_id)
    cart_item = Cart_item.objects.get(cart = cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


# this functions deletes a cart_item from the cart
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id= product_id)
    cart_item = Cart_item.objects.get(cart = cart, product=product)
    cart_item.delete()
    return redirect('cart')

# this function handles the display on the cart page.
def carts(request, total=0, quantity =0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = Cart_item.objects.filter(cart = cart, is_active=True)
        for item in cart_items:
            total  += ( item.product.price * item.quantity )
            quantity += item.quantity
        tax = (0.5*total)/100
        grand_total = total + tax
    except object.DoesNotExist:
        pass

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax':tax,
        'grand_total':grand_total
    }

    return render(request, 'store/cart.html',context)

# Create your views here.
