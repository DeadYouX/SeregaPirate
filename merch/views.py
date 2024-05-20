from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.decorators import login_required


def merch(request):
    return redirect('products')

@login_required
def products(request):
    products = Product.objects.all()
    cart, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), now=True)
    if created:
        cart.save()
    data = {
        "title": 'Товары',
        'showprofile': True,
        'now': 'merch',
        'item': 'product',
        'cart': cart,
        'products': [[obj.id, obj.name, obj.color, str(obj.photo).replace('merch/static/', ''), obj.price] for obj in products],
    }
    return render(request, 'merch/merch.html', data)

@login_required
def cart(request):
    products = Product.objects.all()
    cart, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), now=True)
    if created:
        cart.save()
    if request.method == 'POST':
            try:
                if 'decrease' in request.POST:
                    item_id = request.POST['decrease']
                    if item_id.isdigit():
                        c_item = CartItem.objects.get(id=item_id)
                        if c_item.quantity > 1:
                            c_item.quantity -= 1
                            c_item.save()
                        elif c_item.quantity == 1:
                            c_item.delete()
                        else:
                            c_item.quantity = 1
                            c_item.save()
                if 'increase' in request.POST:
                    item_id = request.POST['increase']
                    if item_id.isdigit():
                        c_item = CartItem.objects.get(id=item_id)
                        c_item.quantity += 1
                        c_item.save()
                if 'cart_payment' in request.POST:
                    if len(cart.items.all()) != 0:
                        return redirect('cart_payment')
            except:
                pass

    data = {
        "title": 'Товары',
        'showprofile': True,
        'now': 'merch',
        'item': 'cart',
        'cart': cart,
        'items': [[ item.product.id, item.id, item.product.name, item.product.color, str(item.product.photo).replace('merch/static/', ''), item.product.price, item.quantity, item.size, item.total_price()] for item in cart.items.all()],
        'products': [[obj.name, obj.color, str(obj.photo).replace('merch/static/', ''), obj.price] for obj in products],
    }
    return render(request, 'merch/cart.html', data)

@login_required
def product_by_id(request, p_id):
    products = Product.objects.filter(id=p_id)
    product = Product.objects.get(id=p_id)
    cart, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), now=True)
    message = ''
    if created:
        cart.save()
    if request.method == 'POST':
        if 'goto_prod' in request.POST:
            return redirect('products')
        elif 'goto_cart' in request.POST:
            return redirect('cart')
        elif 'add_cart' in request.POST:
            len_sizes = len(product.get_size_choices())
            sizes_now = len_sizes
            for size in request.POST:
                if "size" in size:
                    if request.POST[size] == "1":
                        sizes_now -= 1
                        size = size.replace("size", '')
                        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart, size=size)
                        if created:
                            cart_item.save()
                        else:
                            cart_item.quantity += 1
                            cart_item.save()
                        message = f'Товар (размер {size}) добавлен в корзину. Сейчас в корзине: {cart_item.quantity}шт.'
            if sizes_now == len_sizes and message == '':
                message = 'Выберите один размер, прежде чем добавить товар в корзину!'
    data = {
        "title": 'Товары',
        'showprofile': True,
        'now': 'merch',
        'item': 'cart',
        'cart': cart,
        'message': message,
        'sizes': product.get_size_choices(),
        'products': [[obj.id, obj.name, obj.color, str(obj.photo).replace('merch/static/', ''), obj.price] for obj in products],
    }
    return render(request, 'merch/product.html', data)

@login_required
def cart_payment(request):
    cart, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), now=True)
    if created: cart.save()
    if request.method == 'POST':
        if 'back' in request.POST:
            return redirect('cart')
        if 'confirm' in request.POST:
            if request.POST['adress'] != '':
                s = 'Способ доставки: '
                if request.POST['dostavka'] == 'home':
                    s += 'Доставка на дом\n'
                elif request.POST['dostavka'] == 'mail':
                    s += 'Доставка на почту\n'
                s += f'По адресу: {request.POST["adress"]}\n'
                s += f"Удобное время получения: С {5+3*int(request.POST['time'])}:00 до {5+3*int(request.POST['time']) + 3}:00\n"
                cart_last, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), last=True)
                cart_last.last = False
                cart_last.save()
                cart.adress = s
                cart.now = False
                cart.last = True
                cart.save()
                profile = Profile.objects.get(user=request.user)
                profile.purchase_count += 1
                profile.save()
                return redirect('cart_confirm')


    data = {
        "title": 'Товары',
        'showprofile': True,
        'now': 'merch',
        'item': 'cart',
        'cart': cart,
    }
    return render(request, 'merch/cart-payment.html', data)

@login_required
def cart_confirm(request):
    cart, created = Cart.objects.get_or_create(user=Profile.objects.get(user=request.user), last=True)
    if created: cart.save()
    data = {
        "title": 'Товары',
        'showprofile': True,
        'now': 'merch',
        'item': 'cart',
        'adress': str(cart.adress).split('\n'),
    }
    return render(request, 'merch/cart-confirm.html', data)