
from firstapp.models import Restaurant,Food_item
from django.contrib.auth import authenticate,alogin
from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import RestaurantForm
 
# def addRestaurant(request):
#     form=RestaurantForm
#     context={'form':form}
#     return render (request,'Rsignup.html')

def saveRestaurant(request):
    return render (request,'login.html')
def registerRestaurant(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        open=request.POST.get('open')
        close=request.POST.get('close')
        password=request.POST.get('password')
        # in below first name for form name field and second name is variable which is mentioned above

        new_restaurant=Restaurant(name=name,email=email,address=address,mobile_no=mobile,open_time=open,close_time=close,password=password)
        new_restaurant.save()
    return render (request,'Rsignup.html')

def login_restaurant(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        restaurant=Restaurant.objects.all()
        for restro in restaurant:
            if email==restro.email:
                if password==restro.password:
                    # alogin(request,restro)
                    request.session['email']=email
                    request.session['name']=restro.name
                    return render(request,'base.html')
                else:
                    messages.info(request,"Invalid password")
                    return render(request,"login.html")
            
    
        messages.info(request,"user does not exist")
        return render(request,"login.html") 
    else:
        return render(request,"login.html") 
    
def menu(request):
    email=request.session['email']
    name=request.session['name']
    restaurant=Restaurant.objects.get(email=email)
    print(restaurant)
    food_item=Food_item.objects.filter(restaurant=restaurant)
    print(food_item)
    data={
        'food_item':food_item,
        'restaurant':restaurant,
    }
    return render(request,'my_menu.html',data)