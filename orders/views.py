# orders/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm
from .models import Order, OrderItem
from shop.models import Product  # ваша модель товара
from cart.cart import Cart  # если есть класс Cart для сессии

def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                card_number=form.cleaned_data['card_number'],
                bank=form.cleaned_data['bank'],
            )
            for prod_id, info in cart.items():
                product = Product.objects.get(id=prod_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=info['quantity'],
                    price=info['price']
                )
            request.session['cart'] = {}
            # Вместо messages.success:
            request.session['order_success'] = True
            return redirect('/')
    else:
        form = OrderForm()
    return render(request, 'orders/checkout.html', {'form': form})
