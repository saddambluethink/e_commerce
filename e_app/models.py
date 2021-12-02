from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
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
    discount=models.IntegerField(default=5)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    
    def get_all_products():
        return Product.objects.all()

    
    
    def get_products_by_category(category):
        return Product.objects.filter(category=category)





class cartitem(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)



class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



# class checkout(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     cartitem=models.ForeignKey(cartitem,on_delete=models.CASCADE)


#     def __str__(self):
#         return self.user.username
    


class rating(models.Model):
    user=models.ForeignKey(User, on_delete=CASCADE)
    product=models.ForeignKey(Product, on_delete=CASCADE)
    prating=models.IntegerField()

    def __str__(self):
        return self.product.productname







class Customer(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    gender=models.CharField( max_length=10,choices=gen)




