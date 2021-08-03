from django.db import models
from reglog.models import User



class Product(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='media')
    product_location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        self.name


class Order(models.Model):
    user = models.ForeignKey( User, related_name='orders', on_delete=models.CASCADE)
    total_price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     self.total_price


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='carts',on_delete=models.CASCADE)
    orders = models.ForeignKey(Order, related_name='carts', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    products = models.ForeignKey( Product, related_name='carts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     self.quantity
