from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # Забираем флаг order_success из сессии, если он есть
    order_success = request.session.pop('order_success', False)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
        'order_success': order_success,  # <-- добавляем в контекст
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def index(request):
    products = Product.objects.all()
    # Получаем корзину, например, из сессии:
    cart = request.session.get('cart', {}) # словарь вида {'1': {'quantity': 2}, ...}
    cart_items = []
    total = 0

    for prod_id, info in cart.items():
        try:
            product = Product.objects.get(id=prod_id)
            quantity = info['quantity']
            cart_items.append({
                'name': product.name,
                'quantity': quantity,
                'price': product.price,
            })
            total += quantity * product.price
        except Product.DoesNotExist:
            continue

    context = {
        'products': products,
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'shop/index.html', context)


