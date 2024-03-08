
from firstapp.models import Restaurant,Food_item,Customer
# from django.contrib.auth import authenticate,alogin
from django.shortcuts import render,redirect
from django.contrib import messages
# from .forms import RestaurantForm

def saveRestaurant(request):
    return render (request,'Clogin.html')
def registerRestaurant(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        open=request.POST.get('open')
        close=request.POST.get('close')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        # in below first name for form name field and second name is variable which is mentioned above
        restaurant=Restaurant.objects.all()
        for restro in restaurant:
            if email==restro.email:
                messages.info(request,"Restaurant already exist")
                return render(request,"Rsignup.html")   
        new_restaurant=Restaurant(name=name,email=email,address=address,mobile_no=mobile,open_time=open,close_time=close,image=image,password=password)
        new_restaurant.save()
    return render (request,'Rhome.html')

def registerCustomer(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
       
        new_customer=Customer()
        new_customer.name=name
        new_customer.email=email
        new_customer.address=address
        new_customer.mobile_no=mobile
        new_customer.password=password
        new_customer.save()
    return render (request,'base.html')

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
            
    
        messages.info(request,"Restaurant does not exist")
        return render(request,"login.html") 
    else:
        return render(request,"login.html") 


def login_customer(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.all()
        for c1 in customer:
            if email==c1.email:
                if password==c1.password:
                    # alogin(request,restro)
                    request.session['email']=c1.email
                    request.session['name']=c1.name
                    restaurant=Restaurant.objects.all()
                    customer=Customer.objects.get(email=c1.email)
                    data={
                        'restaurant':restaurant,
                        'customer':customer,
                    }
                    
                    return render(request,'Cbase.html',data)
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
    food_item=Food_item.objects.filter(restaurant=restaurant)
    data={
        'food_item':food_item,
        'restaurant':restaurant,
    }
    return render(request,"my_menu.html",data)

def edit(request,item_id):
    email=request.session['email']
    name=request.session['name']
    request.session['item_id']=item_id
    food_item = Food_item.objects.get(pk=item_id)
    print(food_item.name)
    restaurant=Restaurant.objects.get(email=email)
    
    data={
        'food_item':food_item,
        'restaurant':restaurant,
    }
    return render(request,"edit.html",data)

def edit_food(request):
    item_id=request.session['item_id']
    food_item = Food_item.objects.get(pk=item_id)
    # restaurant=Restaurant.objects.get(restaurant=food_item.restaurant)
    request.session['email']=food_item.restaurant.email
    request.session['name']=food_item.restaurant.name
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        category=request.POST.get('category')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        food_item.name=name
        food_item.price=price
        food_item.category=category
        food_item.description=description
        food_item.image=image
        food_item.save()
        return redirect('menu')
    else:
        return redirect('menu')
    

def add_item(request):
    email=request.session['email']
    name=request.session['name']
    restaurant=Restaurant.objects.get(email=email)
    data={
        'restaurat':restaurant,
    }
    return render(request,'add_item.html',data)

def add_menu(request):
    email=request.session['email']
    name=request.session['name']
    restaurant=Restaurant.objects.get(email=email)
    item=Food_item()
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        category=request.POST.get('category')
        description=request.POST.get('description')
        image=request.FILES.get('image')
        item.name=name
        item.price=price
        item.restaurant=restaurant
        item.category=category
        item.description=description
        item.image=image
        print(item.image)
        item.save()
        return redirect('menu')
    else:
         return redirect('menu')
    

def cprofile(request):
    email=request.session['email']
    name=request.session['name']
    customer=Customer.objects.get(email=email)
    data={
        'customer':customer,
    }
    return render(request,"Cprofile.html",data)

    
  