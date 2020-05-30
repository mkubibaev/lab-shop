from django.shortcuts import render, redirect


def index_view(request):
    return redirect(products_list_view)


def products_list_view(request):
    return render(request, 'products_list.html')
