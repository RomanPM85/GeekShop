from django.contrib import admin

from mainapp.models import ProductCategory, Product

admin.site.register(ProductCategory)
#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
    readonly_fields = ('price',)
    ordering = ('price',)
    search_fields = ('name', 'category__name', 'price', 'quantity')