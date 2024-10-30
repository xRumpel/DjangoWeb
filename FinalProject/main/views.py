from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from telegram import Bot
from .forms import UserForm
from .models import Product
from .forms import OrderForm

def index(request):
    return render(request, 'main/index.html', {'caption': 'Доставка цветов'})

def new(request):
    return render(request, 'main/new.html')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserForm()
    return render(request, 'main/register.html', {'form': form})

def success(request):
    return render(request, 'main/success.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'main/product_list.html', {'products': products})

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'main/place_order.html', {'form': form})

def order_success(request):
    return render(request, 'main/order_success.html')