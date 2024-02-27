from django.contrib import admin

# Register your models here.
from .models import Restaurant,Customer,Order,Product,Cart,Payment,Feedback
class restaurant_admin(admin.ModelAdmin):
    list_display=('Name','Email','Address','mobile_no','open_time','close_time')

class customer_admin(admin.ModelAdmin):
    list_display=('Name','Email','Address','mobile_no')

class product_admin(admin.ModelAdmin):
    list_display=('name','restaurant_id','price','category','description')

class cart_admin(admin.ModelAdmin):
    list_display=('product_id','quantity')

class payment_admin(admin.ModelAdmin):
    list_display=('customer_id','cart_id','upi','upi_id','debit_card_no')

class order_admin(admin.ModelAdmin):
    list_display=('customer_id','cart_id')

class feedback_admin(admin.ModelAdmin):
    list_display=('rating','customer_id','product_id')


admin.site.register(Restaurant,restaurant_admin)
admin.site.register(Customer,customer_admin)
admin.site.register(Product,product_admin)
admin.site.register(Cart,cart_admin)
admin.site.register(Payment,payment_admin)
admin.site.register(Order,order_admin)
admin.site.register(Feedback,feedback_admin)