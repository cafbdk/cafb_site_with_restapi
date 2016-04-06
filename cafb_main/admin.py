from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = Product._meta.get_all_field_names() #all class model attrs

admin.site.register(Product, ProductAdmin)
