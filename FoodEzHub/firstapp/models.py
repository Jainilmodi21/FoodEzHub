from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    open_time=models.TimeField()
    close_time=models.TimeField()
    password=models.CharField(max_length=30,default='')
    image = models.ImageField(upload_to='images/',default='')

class Customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    address=models.CharField(max_length=50)
    mobile_no=models.CharField(max_length=10)
    password=models.CharField(max_length=30,default='')


class Food_item(models.Model):
    name=models.CharField(max_length=30)
    restaurant=models.ForeignKey(Restaurant,null=False,on_delete=models.CASCADE)
    price=models.IntegerField()
    category=models.CharField(max_length=30)
    description=models.CharField(max_length=60)
    image = models.ImageField(upload_to='images/',default='')
    
class Cart(models.Model):
     product=models.ForeignKey(Food_item,null=False,on_delete=models.CASCADE)
     quantity=models.IntegerField()

class Payment(models.Model):
    customer=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,null=False,on_delete=models.CASCADE)
    upi=models.IntegerField()
    upi_id=models.CharField(max_length=30)
    debit_card_no=models.IntegerField()


class Order(models.Model):
    customer=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    cart_id=models.ForeignKey(Cart,null=False,on_delete=models.CASCADE)


class Feedback(models.Model):
    rating=models.IntegerField()
    customer=models.ForeignKey(Customer,null=False,on_delete=models.CASCADE)
    product=models.ForeignKey(Food_item,null=False,on_delete=models.CASCADE)
