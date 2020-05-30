"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from webapp.views import products_list_view, index_view, product_view, product_add_view, product_edit_view

urlpatterns = [
    path('', index_view, name='index'),
    path('products', products_list_view, name='products_list'),
    path('products/add', product_add_view, name='product_add'),
    path('products/<int:pk>', product_view, name='product'),
    path('products/<int:pk>/edit', product_edit_view, name='product_edit'),
    path('admin/', admin.site.urls),
]

