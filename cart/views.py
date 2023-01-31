from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from products.models import Product
from .cart import Cart
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True
        })

    context = {'cart': cart}
    return render(request, 'cart/cart_details.html', context)


@require_POST
def add_to_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleand_data = form.cleaned_data
        quantity = cleand_data['quantity']
        inplace = cleand_data['inplace']
        cart.add(product, quantity, inplace)

    return redirect('cart_detail')


@require_POST
def remove_from_cart_view(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')
