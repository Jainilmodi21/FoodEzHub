from django.shortcuts import render
from firstapp.models import Restaurant

from django.shortcuts import render
# from .forms import RestaurantForm
 
# def addRestaurant(request):
#     form=RestaurantForm
#     context={'form':form}
#     return render (request,'Rsignup.html')

def saveRestaurant(request):
    return render (request,'Rsignup.html')
def sd(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        open=request.POST.get('open')
        close=request.POST.get('close')
        password=request.POST.get('password')
        # in below first name for form name field and second name is variable which is mentioned above

        new_restaurant=Restaurant(Name=name,Email=email,Address=address,mobile_no=mobile,open_time=open,close_time=close,password=password)
        new_restaurant.save()
    return render (request,'Rsignup.html')
