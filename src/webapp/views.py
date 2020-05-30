from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ProductForm, SearchForm
from webapp.models import Product


def index_view(request):
    return redirect('products_list')


def products_list_view(request):
    products = Product.objects.filter(amount__gt=0)
    form = SearchForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data['search']
        if search_query:
            products = products.filter(name__icontains=search_query)
    products = products.order_by('category', 'name')
    return render(request, 'products_list.html', context={'products': products, 'form': form})


def product_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product})


def product_add_view(request):
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


def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'amount': product.amount,
            'price': product.price
        })
        return render(request, 'product_edit.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.amount = form.cleaned_data['amount']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('product', pk=product.pk)
        else:
            return render(request, 'product_edit.html', context={'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'product_delete.html', context={'product': product})
    elif request.method == 'POST':
        product.delete()
        return redirect('products_list')
