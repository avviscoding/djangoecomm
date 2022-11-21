from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@login_required(login_url = 'account:login')
def products_home(request):

    all_category = Category.objects.all()

    if request.method == 'POST':
        if 'search_product' in request.POST:
            search = request.POST['search_product']
            if search != '':
                all_products_fashion = Product.objects.filter(product_name__icontains=search)
            else:
                all_products_fashion = Product.objects.all()
    else:
        all_products_fashion = Product.objects.all()

    context = {
        'all_products_fashion':all_products_fashion,
        'all_category':all_category,
    }
    return render(request, 'products/products_home.html', context)
