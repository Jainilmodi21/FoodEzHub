from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('Csignup',views.Csignup,name='Csignup'),
    path('Rsignup',views.Rsignup,name='Rsignup'),
    path('login',views.login,name='login'),
    path('about',views.about,name='about'),
    path('rabout',views.rabout,name='rabout'),
    path('registerRestaurant',views.registerRestaurant,name='registerRestaurant'),
    path('login_all',views.login_all,name='login_all'),
    path('registerCustomer',views.registerCustomer,name='registerCustomer'),
    path('menu',views.menu,name='menu'),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('edit_food', views.edit_food, name='edit_food'),
    path('add_item',views.add_item,name='add_item'),
    path('add_menu',views.add_menu,name='add_menu'),
    path('cprofile',views.cprofile,name='cprofile'),
    path('rprofile',views.rprofile,name='rprofile'),
    path('restro_menu/<int:restro_id>/', views.restro_menu, name='restro_menu'),
    path('search',views.search,name='search'),
    path('edit_profile',views.edit_profile,name="edit_profile"),
    path('redit_profile',views.redit_profile,name="redit_profile"),
    path('update_profile',views.update_profile,name="update_profile"),
    path('rupdate_profile',views.rupdate_profile,name="rupdate_profile"),
    path('delete/<int:item_id>/', views.delete, name='delete'),
    path('add_cart', views.add_cart, name='add_cart'),
    path('history',views.history,name='history'),
    path('proceed', views.proceed, name='proceed'),
    path('cbase', views.cbase, name='cbase'),
    path('restro_home', views.restro_home, name='restro_home'),
    path('current_order/<int:order_id>/',views.current_order,name='current_order'),
    path('prepare_order/<int:order_id>/',views.prepare_order,name='prepare_order'),
    path('reject_order/<int:order_id>/',views.reject_order,name='reject_order'),
    path('rating/<int:order_id>/',views.rating,name='rating'),
]
