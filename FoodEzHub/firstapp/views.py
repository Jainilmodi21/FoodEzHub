
from firstapp.models import Restaurant,Food_item,Customer,Cart,Cart_item,Order,Feedback,Payment
# from django.contrib.auth import authenticate,alogin     
from django.shortcuts import render,redirect
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta
import razorpay
from FoodEzHub.settings import RAZOR_PAY_KEY_ID,KEY_SECRET


# from .forms import RestaurantForm

def index(request):
    return render (request,'index.html')

def Csignup(request):
    return render (request,'Csignup.html')


def Rsignup(request):
    return render (request,'Rsignup.html')

def about(request):
    return render(request,'cabout.html')

def rabout(request):
    return render(request,'rabout.html')

def login(request):
    return render (request,'login.html')

def cbase(request):
      email=request.session['email']
      name=request.session['name']
      
      restaurant=Restaurant.objects.all()
      customer1=Customer.objects.get(email=email)
      data={
        'restaurant':restaurant,
        'customer':customer1,
        }
      return render(request,"chome.html",data)




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
    return render(request,"login.html")

def login_all(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.objects.all()
        restaurant=Restaurant.objects.all()

        for r1 in restaurant:
            if email==r1.email:
                if password==r1.password: 
                    request.session['email']=email                     
                    return redirect("restro_home")
                else:
                    messages.info(request,"Invalid password")
                    return render(request,"Rlogin.html")      

        for c1 in customer:
            if email==c1.email:
                if password==c1.password:
                    request.session['email']=c1.email
                    request.session['name']=c1.name
                    customer1=Customer.objects.get(email=c1.email)
                    data={
                        'restaurant':restaurant,
                        'customer':customer1,
                    }
                    return render(request,'chome.html',data)
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
    food_item=Food_item.objects.filter(restaurant=restaurant)
    
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
        flag=0
        name=request.POST.get('name')
        price=request.POST.get('price')
        category=request.POST.get('category')
        description=request.POST.get('description')
        if(request.FILES.get('image1')):
            image=request.FILES.get('image1')
            flag=1
        food_item.name=name
        food_item.price=price
        food_item.category=category
        if(flag):
            food_item.image=image
        food_item.description=description
        
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

def rprofile(request):
    email=request.session['email']
    restaurant=Restaurant.objects.get(email=email)
    data={
        'restaurant':restaurant,
    }
    return render(request,"rprofile.html",data)

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


def redit_profile(request):
    email=request.session['email']
    restaurant=Restaurant.objects.get(email=email)
    data={
        'restaurant':restaurant,
    }
    return render(request,"redit.html",data)


def update_profile(request):
    email=request.session['email']
    name=request.session['name']
    if request.method=="POST":
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        address1=request.POST.get('address')
        mobile1=request.POST.get('mobile_no')
        customer=Customer.objects.get(email=email)
        customer.name=name1
        customer.email=email1
        customer.address=address1
        customer.mobile_no=mobile1
        customer.save()
    return render(request,"login.html")

def rupdate_profile(request):
    email=request.session['email']
    if request.method=="POST":
        flag=0
        flag1=0
        name1=request.POST.get('name')
        email1=request.POST.get('email')
        address1=request.POST.get('address')
        mobile1=request.POST.get('mobile_no')
        if(request.POST.get('open')):
            open=request.POST.get('open')
            flag=1
        if(request.POST.get('close')):
            close=request.POST.get('close')
            flag1=1
        restaurant=Restaurant.objects.get(email=email)
        restaurant.name=name1
        restaurant.email=email1
        restaurant.address=address1
        restaurant.mobile_no=mobile1
        if(flag):
            restaurant.open_time=open
        if(flag1):
            restaurant.close_time=close
        restaurant.save()
    return render(request,"login.html")



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
        cart.restaurant=restaurant
        cart.save()
        food=Food_item.objects.filter(restaurant=restaurant)
        i=1
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
        request.session['cart_id']=cart.pk 
        cart_item=Cart_item.objects.filter(cart=cart)
        client=razorpay.Client(auth=(RAZOR_PAY_KEY_ID,KEY_SECRET))
        data = { "amount": (cart.total_amount)*100, "currency": "INR", "payment_capture": "1" }    
        payment = client.order.create(data=data)
        cart.razor_pay_order_id=payment['id']
        cart.save()
        data={
            'cart_item':cart_item,
             'cart':cart,
             'restaurant':restaurant,
             'payment':payment,
        }
        return render(request,"cart.html",data)

def proceed(request):
        cart_id=request.session['cart_id']
        cart=Cart.objects.get(pk=cart_id)
        order=Order()
        order.cart=cart
        order.date=date.today()
        order.status="pending"
        order.save()
        payment=Payment()
        payment.customer=cart.customer
        payment.cart=cart
        payment.method="COD"
        payment.save()
       
        return  redirect("cbase")

def history(request):
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    cart=Cart.objects.filter(customer=customer)
    order=Order.objects.filter(cart__customer=customer)
    data={
        'cart':cart,
        'order':order,
        'customer':customer,

    }
    return render(request,"history.html",data)

def restro_home(request):
    email=request.session['email']
    restaurant=Restaurant.objects.get(email=email)

    order1=Order.objects.filter(status="pending") & Order.objects.filter(cart__restaurant=restaurant)
    order2=Order.objects.filter(status="processing") & Order.objects.filter(cart__restaurant=restaurant)
    order3=Order.objects.filter(status="delivered") & Order.objects.filter(cart__restaurant=restaurant)
    total_order=0
    total_revenue=0
    for i in order3:
        if i.order_date==date.today():
            total_revenue+=i.cart.total_amount
            total_order+=1
            
    data={
        'order1':order1,
        'order2':order2,
        'total_order':total_order,
        'total_revenue':total_revenue,
        'restaurant':restaurant,
       
    }
    return render(request,"Rhome.html",data)

def current_order(request,order_id):
    order=Order.objects.get(pk=order_id)
    order.status="processing"
    order.save()
    return redirect("restro_home")

def prepare_order(request,order_id):
    order=Order.objects.get(pk=order_id)
    order.status="delivered"
    order.save()
    return redirect("restro_home")

def reject_order(request,order_id):
    order=Order.objects.get(pk=order_id)
    order.status="rejected"
    order.save()
    return redirect("restro_home")

def rating(request,order_id):
    order=Order.objects.get(pk=order_id)
    customer=order.cart.customer
    restaurant=order.cart.restaurant
    if request.method=="POST":
        rating=request.POST.get('rating')
        total_item=0
        total_rating=0
        feedback=Feedback()
        feedback.order=order
        feedback.customer=customer
        feedback.restaurant=restaurant
        feedback.rating=rating
        feedback.save()
        feedback1=Feedback.objects.filter(restaurant=restaurant)
        for i in feedback1:
            total_item+=1
            total_rating+=i.rating
        rat=total_rating/total_item
        restaurant.rating = round(rat, 1)
        restaurant.save()
        return redirect("cbase")


    





    
