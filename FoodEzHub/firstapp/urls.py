from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.saveRestaurant,name='saveRestaurant'),
    # path('admin/', admin.site.urls),
  
    path('sd/',views.sd,name='sd')
    

]
