from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm
from webapp.models import Product


def index_view(request):
    return redirect('products_list')


def products_list_view(request):
    products = Product.objects.filter(amount__gt=0).order_by('category', 'name')
    return render(request, 'products_list.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def product_add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'product_add.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product = Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                amount=form.cleaned_data['amount'],
                price=form.cleaned_data['price']
            )
            return redirect('product', pk=product.pk)
        else:
            return render(request, 'product_add.html', context={'form': form})
