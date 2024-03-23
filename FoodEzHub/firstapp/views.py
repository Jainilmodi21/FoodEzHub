
from firstapp.models import Restaurant,Food_item,Customer,Cart,Cart_item
# from django.contrib.auth import authenticate,alogin
from django.shortcuts import render,redirect
from django.contrib import messages

# from .forms import RestaurantForm

def index(request):
    return render (request,'index.html')

def Csignup(request):
    return render (request,'Csignup.html')


def Rsignup(request):
    return render (request,'Rsignup.html')


def login(request):
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
        image=request.FILES.get('image')
        # in below first name for form name field and second name is variable which is mentioned above
        restaurant=Restaurant.objects.all()
        for restro in restaurant:
            if email==restro.email:
                messages.info(request,"Restaurant already exist")
                return render(request,"Rsignup.html")   
        new_restaurant=Restaurant(name=name,email=email,address=address,mobile_no=mobile,open_time=open,close_time=close,image=image,password=password)
        new_restaurant.save()
    return render (request,'login.html')

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
    return render (request,'Clogin.html')

 


def login_all(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.all()
        restaurant=Restaurant.objects.all()

        for r1 in restaurant:
            if email==r1.email:
                if password==r1.password:
                    request.session['email']=r1.email
                    request.session['name']=r1.name
                    restaurant1=Restaurant.objects.get(email=r1.email)
                
                    data={
                        'restaurant':restaurant1,
                        # 'customer':customer,
                    }
                    
                    return render(request,'base.html',data)
                else:
                    messages.info(request,"Invalid password")
                    return render(request,"Rlogin.html")
            
    
        # messages.info(request,"user does not exist")
       

        for c1 in customer:
            if email==c1.email:
                if password==c1.password:
                    request.session['email']=c1.email
                    request.session['name']=c1.name
                    # restaurant=Restaurant.objects.all()
                    customer1=Customer.objects.get(email=c1.email)
                    data={
                        'restaurant':restaurant,
                        'customer':customer1,
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

def delete(request,item_id):
    email=request.session['email']
    name=request.session['name']
    request.session['item_id']=item_id
    
    food_item1 = Food_item.objects.get(pk=item_id)
    food_item1.delete()
    restaurant=Restaurant.objects.get(email=email)
    food_item=Food_item.objects.all()
    
    data={
        'food':food_item1,
        'food_item':food_item,
        'restaurant':restaurant,
    }
    return render(request,"my_menu.html",data)

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

def restro_menu(request,restro_id):
    email=request.session['email']
    name=request.session['name']
    request.session['restro_id']=restro_id
    restaurant = Restaurant.objects.get(pk=restro_id)
  
    food_item=Food_item.objects.filter(restaurant=restaurant)
    data={
        'restaurant':restaurant,
        'food_item':food_item,
    }
    return render(request,"restro_menu.html",data)

def search(request):
    if request.method=="POST":
        search=request.POST.get('search')
        restaurant=Restaurant.objects.filter(name=search)
        data={
            'search':restaurant
        }
        return render(request,"Cbase.html",data)

def edit_profile(request):
    email=request.session['email']
    name=request.session['name']
    customer=Customer.objects.get(email=email)
    data={
        'customer':customer,
    }
    return render(request,"edit_profile.html",data)


def update_profile(request):
    email=request.session['email']
    name=request.session['name']
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        address1=request.POST.get('address')
        mobile1=request.POST.get('mobile')
    
    customer=Customer.objects.get(email=email)
    customer.name=name1
    customer.email=email1
    customer.address=address1
    customer.mobile_no=mobile1
    customer.save()


def add_cart(request):
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    if request.method=='POST':
        restro_id=request.session['restro_id']
        restaurant=Restaurant.objects.get(pk=restro_id)
        print(restaurant)
        cart=Cart()
        cart.customer=customer
        cart.total_item=0
        cart.total_amount=0
        cart.save()
        food=Food_item.objects.filter(restaurant=restaurant)
        # retrive data from html
        i=1
        # total food item in cart j
        j=0
        total=0
        for fd in food:
            quantity=int(request.POST.get(f'{i}_quantity'))
            if fd and quantity>0:
                j+=1
                cart_item=Cart_item()
                cart_item.food_item=fd
                cart_item.quantity=quantity
                cart_item.cart=cart
                amount=quantity*fd.price
                cart_item.amount=amount
                cart_item.save()
                total+=amount

            i+=1
        
        cart.total_item=j
        cart.total_amount=total
        cart.save()
       
           
        cart_item=Cart_item.objects.filter(cart=cart)


        data={
            'cart_item':cart_item,
             'cart':cart,
             'restaurant':restaurant,
        }
        
        return render(request,"cart.html",data)


    
