from django.contrib import admin
from .models import Store, Category,Customer,Order,OrderItem,Cart,Ship_Add
# Register your models here.
admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Ship_Add)