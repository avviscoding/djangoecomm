from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url = 'account:login')
def products_home(request):
    all_products = Product.objects.all()
    context = {
        'all_products':all_products,
    }
    return render(request, 'products/products_home.html', context)

