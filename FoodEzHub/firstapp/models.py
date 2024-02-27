from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Address=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    open_time=models.TimeField()
    close_time=models.TimeField()
    password=models.CharField(max_length=30,default='')

class Customer(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField(max_length=30)
    Address=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    password=models.CharField(max_length=30,default='')


class Product(models.Model):
    name=models.CharField(max_length=30)
    restaurant_id=models.ForeignKey(Restaurant,null=False,on_delete=models.CASCADE)
    price=models.IntegerField()
    category=models.CharField(max_length=30)
    description=models.CharField(max_length=60)
    
class Cart(models.Model):
     product_id=models.ForeignKey(Product,null=False,on_delete=models.CASCADE)
     quantity=models.IntegerField()

class Payment(models.Model):
    customer_id=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,null=False,on_delete=models.CASCADE)
    upi=models.IntegerField()
    upi_id=models.CharField(max_length=30)
    debit_card_no=models.IntegerField()


class Order(models.Model):
    customer_id=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,null=False,on_delete=models.CASCADE)


class Feedback(models.Model):
    rating=models.IntegerField()
    customer_id=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,null=False,on_delete=models.CASCADE)
