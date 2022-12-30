from django.db import models

# Create your models here.
class Products(models.Model):
    
    Product_name=models.CharField(max_length=100)
    lowcost=models.IntegerField()
    last_update=models.DateTimeField()

class Product_variations(models.Model):
       
    prodct_id=models.IntegerField(default=999)
    variation=models.CharField(max_length=200)
    stock=models.IntegerField()
    last_update=models.DateTimeField()

