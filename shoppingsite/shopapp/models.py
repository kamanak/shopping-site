from distutils.command.upload import upload
import email
from email.mime import image
from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200,null=True,blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="products")
    marked_price = models.PositiveIntegerField()
    selling_price = models.PositiveBigIntegerField()
    description = models.TextField()
    warranty = models.CharField(max_length=200,null=True,blank=True)
    return_policy = models.CharField(max_length=200,null=True,blank=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    total = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class CartProduct(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    sub_total = models.PositiveIntegerField()

ORDER_STATUS = (
    ("Order Received","Order Received"),
    ("Order Processing","Order Processing"),
    ("On the way","On the way"),
    ("Order Completed","Order Completed"),
    ("Order Cancelled","Order Cancelled")
)


class Order(models.Model):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True,blank=True)
    sub_total = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=200,choices=ORDER_STATUS)








