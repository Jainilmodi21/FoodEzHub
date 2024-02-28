from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.saveRestaurant,name='saveRestaurant'),
    # path('admin/', admin.site.urls),
  
    path('registerRestaurant',views.registerRestaurant,name='registerRestaurant'),
    path('login_restaurant',views.login_restaurant,name='login_restaurant'),
    path('menu',views.menu,name='menu'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('edit_food', views.edit_food, name='edit_food'),
    path('add_item',views.add_item,name='add_item'),
    path('add_menu',views.add_menu,name='add_menu'),
]
