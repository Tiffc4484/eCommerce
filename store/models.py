from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    customer_name = models.CharField(max_length=200, null=True)
    gender = models.BooleanField(default=True, null=True)
    phone = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    cost = models.FloatField(null=True)
    is_on_sale = models.BooleanField(default=False, null=True, blank=False)
    available_stock = models.FloatField(null=True)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False, null=True, blank=False)
    total_price = models.FloatField(default=0, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.product_count for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    product_count = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.product_count
        return total
