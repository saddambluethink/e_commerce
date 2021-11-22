from django.db import models

# Create your models here.
choices=[
    ('man','man'),
    ('woman','woman'),
    ('child','child'),
    ('vagetable&fruits','vagetable&fruits')
]  
class Product(models.Model):
    productname = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    image=models.ImageField(upload_to='images')
    category=models.CharField( max_length=20,choices=choices)
