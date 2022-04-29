from django.shortcuts import render
from .models import Store

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def products(request):
    product = Store.objects.all()[:12]
    return render(request, 'store/product.html', {'products': product})