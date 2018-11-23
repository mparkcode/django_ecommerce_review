from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from products.models import Product
import json
# Create your views here.

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    cart_total = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
    
        cart_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': product.price * quantity
        })
        cart_total += product.price * quantity
    
    return render(request, "cart/view_cart.html", {'cart_items': cart_items, "cart_total":cart_total})

def add_to_cart(request):
    product_id =request.POST['product']
    quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + quantity
    request.session['cart'] = cart
    return redirect("/")
    
def remove_from_cart(request):
    id = request.POST['product_id']
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect('view_cart')