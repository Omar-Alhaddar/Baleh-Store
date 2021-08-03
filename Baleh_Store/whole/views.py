from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *


def index2(request):

    return render(request, "index.html")


def check(request):
    context = {
        "user": User.objects.get(id=request.session['user_id']),

    }
    return render(request, "checkout.html", context)


def allproducts(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'allproducts.html', context)


def myproducts(request):

    return render(request, "myproducts.html")


def mycart(request):

    return render(request, 'mycart.html')


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    current_user = User.objects.get(id=request.session['user_id'])
    if len(Cart.objects.filter(user=current_user)) > 0:
        cart = Cart.objects.get(user=current_user)
        cart.quantity += 1
        cart.products.add(product)
    else:
        cart = Cart.objects.create(user=current_user)
        cart.quantity += 1
        cart.products.add(product)
    return redirect('/allproducts')


def remove_product(request, product_id):
    product = Product.objects.get(id=product_id)
    current_user = User.objects.get(id=request.session['user_id'])
    cart = Cart.objects.get(user=current_user)
    cart.products.remove(product)
    return redirect('/mycart')


# current_user = User.objects.get(id=request.session['user_id'])
#     try:
#         cart = Cart.objects.get(user=current_user)
#     except Cart.DoesNotExist:
#         cart = None
#     total_price = 0
#     cart_i = cart.products.all()
#     for product in cart.products.all():
#         total_price += product.price
#     sum_products = 0
#     for product in cart.products.all():
#         sum_products += 1
#     context = {
#         'CartProducts': cart.products.all(),
#         'total_cost': total_price,
#         'number_products': sum_products
#     }
def mycart1(request):

    return render(request, 'mycart1.html')

def mycart2(request):

    return render(request, 'mycart2.html')

def mycart3(request):

    return render(request, 'mycart3.html')

def mycart4(request):

    return render(request, 'mycart4.html')

def mycart5(request):

    return render(request, 'mycart5.html')

def mycart6(request):

    return render(request, 'mycart6.html')

def mycart7(request):

    return render(request, 'mycart7.html')

def mycart8(request):

    return render(request, 'mycart8.html')

def mycart9(request):

    return render(request, 'mycart9.html')

def mycart10(request):

    return render(request, 'mycart10.html')

def mycart11(request):

    return render(request, 'mycart11.html')

def mycart12(request):

    return render(request, 'mycart12.html')
