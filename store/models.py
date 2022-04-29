from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email}, {self.customer.address}'

    class Meta:
        db_table = 'customer'


class Category(models.Model):
    title = models.CharField(max_length=255)

class Store(models.Model):
    name = models.CharField(max_length= 200, null=True)
    price = models.DecimalField( max_digits = 6,decimal_places = 2, null=True)
    image_1 = models.URLField(max_length=1000)
    image_alt = models.URLField(max_length=1000)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self): 
        return f' {self.name}'

class Order(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Store, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}'

class Cart(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'