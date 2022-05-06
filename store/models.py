from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.




class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.first_name}, {self.user.last_name}'
    
    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance)
    
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.customer.save()
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender,created,instance, **kwargs):
        try:
            instance.customer.save()
        except ObjectDoesNotExist:
             Customer.objects.create(user=instance)




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
    @property
    def get_cart_sum(self):
         orderitems = self.orderitem_set.all()
         total = sum([item.get_total for item in orderitems])
         return total 
    
    @property
    def get_cart_products(self):
         orderitems = self.orderitem_set.all()
         total = sum([item.quantity for item in orderitems])
         return total 



class OrderItem(models.Model):
	product = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class Cart(models.Model):
    product = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='carts')
    quantity = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product},{self.quantity},{self.created_date}'

class Ship_Add(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	created_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address