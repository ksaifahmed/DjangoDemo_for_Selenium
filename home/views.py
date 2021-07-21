from django.contrib.auth import logout
from django.shortcuts import render, redirect
from home.forms import ProductForm
from home.models import Product
from login.models import CustomUser


def load_home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    username = CustomUser.objects.get(id=request.user.id)
    username = username.email
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            quantity = form.cleaned_data['quantity']
            price = form.cleaned_data['price']
            discount = form.cleaned_data['discount']
            location = form.cleaned_data['location']
            warranty = form.cleaned_data['warranty']

            # data from radio button
            additional_op = form.cleaned_data['additional_options']
            product = Product.objects.create(
                name=name,
                quantity=quantity,
                price=price,
                discount=discount,
                location=location,
                warranty=warranty,
                refund="1" in additional_op,
                exchange="2" in additional_op,
                free_delivery="3" in additional_op,
                free_service="4" in additional_op
            )
            product.save()
            print(additional_op)
            return redirect('home')

    return render(request, 'home.html', {'form': form, 'username': username})


def user_logout(request):
    logout(request)
    return redirect('login')


def history(request):
    if not request.user.is_authenticated:
        return redirect('login')

    username = CustomUser.objects.get(id=request.user.id)
    username = username.email

    product_list = Product.objects.all()
    return render(request, 'product_list.html', {'list': product_list, 'username': username})
