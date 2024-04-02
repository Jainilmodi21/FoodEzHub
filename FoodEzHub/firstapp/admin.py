from django.contrib import admin

# Register your models here.
from .models import Restaurant,Customer,Cart_item,Food_item,Cart,Payment,Feedback,Order
class restaurant_admin(admin.ModelAdmin):
    list_display=('name','email','address','mobile_no','open_time','close_time','rating')

class customer_admin(admin.ModelAdmin):
    list_display=('name','email','address','mobile_no')

class food_item_admin(admin.ModelAdmin):
    list_display=('name','restaurant','price','category','description')

class cart_admin(admin.ModelAdmin):
    list_display=('customer','total_item','total_amount')

class payment_admin(admin.ModelAdmin):
    list_display=('customer','cart','method')

class cart_item_admin(admin.ModelAdmin):
    list_display=('food_item','quantity','amount','cart')

class feedback_admin(admin.ModelAdmin):
    list_display=('rating','customer','restaurant')


class order_admin(admin.ModelAdmin):
    list_display=('cart','order_date','status')


admin.site.register(Restaurant,restaurant_admin)
admin.site.register(Customer,customer_admin)
admin.site.register(Food_item,food_item_admin)
admin.site.register(Cart,cart_admin)
admin.site.register(Payment,payment_admin)
admin.site.register(Cart_item,cart_item_admin)
admin.site.register(Feedback,feedback_admin)
admin.site.register(Order,order_admin)