from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    exclude = []
    search_fields = ['name', 'description', 'price']


admin.site.register(Product, ProductAdmin)
