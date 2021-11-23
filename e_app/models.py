from django.db import models
from django.db.models.fields import CharField, EmailField
from django.utils.html import mark_safe
# Create your models here.
choices=[
    ('man','man'),
    ('woman','woman'),
    ('child','child'),
    ('vagetable&fruits','vagetable&fruits')
]  

gen=[
    ('man','man'),
    ('woman','woman'),
    
]  
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image=models.ImageField(upload_to='images')
    category=models.CharField( max_length=20,choices=choices)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    
    def get_all_products():
        return Product.objects.all()

    
    
    def get_products_by_category(category):
        return Product.objects.filter(category=category)



class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    gender=models.CharField( max_length=10,choices=gen)