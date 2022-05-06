from itertools import product
from urllib import request
from django.shortcuts import render, redirect
from .models import Store, Category, Cart, Order, OrderItem, Ship_Add, Customer
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from store.forms import SignUpForm





# Create your views here.
def search_bar(request):
    if request.method == "POST":
        searched = request.POST.get('searched')
        products = Store.objects.filter(name__contains=searched)
        context = {'searched':searched, 'products':products}
        
        return render(request, 'store/search_bar.html', context)
    else:
        return render(request, 'store/search_bar.html')

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

def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.customer.first_name = form.cleaned_data.get('first_name')
        user.customer.last_name = form.cleaned_data.get('last_name')
        user.customer.address = form.cleaned_data.get('address')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password= password)
        login(request, user)
        return redirect('/')
    return render(request, 'signup.html', {'form': form})