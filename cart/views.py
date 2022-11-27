from django.shortcuts import render, get_object_or_404, redirect
from .models import *
# Create your views here.

def cart(request):
    order = get_object_or_404(Order, user=request.user, ordered=False)
    order_items = order.items.all()

    if request.method == 'POST':
        order_item_id = request.POST['order_item_id']
        order_item_quntity = request.POST['quantity']
        print(order_item_id)
        print(order_item_quntity)
        update_qty = get_object_or_404(OrderItem, id=order_item_id)
        update_qty.quantity = int(order_item_quntity)
        update_qty.save()

    context = {
        'order_items':order_items,
        'order':order,
    }
    return render(request, 'cart/cart.html', context)
