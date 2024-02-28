from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.saveRestaurant,name='saveRestaurant'),
    # path('admin/', admin.site.urls),
  
    path('registerRestaurant',views.registerRestaurant,name='registerRestaurant'),
    path('login_restaurant',views.login_restaurant,name='login_restaurant'),
    path('menu',views.menu,name='menu')
]
