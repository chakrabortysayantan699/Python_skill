from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Product_variations
from .models import Products

admin.site.register(Products)
admin.site.register(Product_variations)

class ProdctAdmin(ImportExportActionModelAdmin):
    list_display=('product_name','lowcost','last_update')

# Register your models here.
