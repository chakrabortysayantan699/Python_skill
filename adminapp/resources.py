from import_export import resources
from .models import Products
from .models import Product_variations

class ProductResource(resources.ModelResource):
    class meta:
        model=Products
class Product_variationResource(resources.ModelResource):
    class meta:
        model=Product_variations