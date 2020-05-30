from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product


def index_view(request):
    return redirect(products_list_view)


def products_list_view(request):
    products = Product.objects.filter(count__gt=0).order_by('category', 'name')
    return render(request, 'products_list.html', context={'products': products})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})
