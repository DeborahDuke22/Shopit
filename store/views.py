from itertools import product
from urllib import request
from django.shortcuts import render
from .models import Store, Category, Cart, Order, OrderItem, Ship_Add, Customer
from django.core.paginator import Paginator


# Create your views here.

def products(request):
    product = Store.objects.all()[:12]
    return render(request, 'store/product.html', {'products': product})
    
def store(request):
    product = Store.objects.all()
    
    paginator = Paginator(product, 12)
    page_list = request.GET.get('page')
    product_list = paginator.get_page(page_list)
    collection = Category.objects.all()
    
    context = {'products':product_list,  'categories':collection}
    return render(request,  'store/store.html', context)



def cart(request):

    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(customer=customer)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

