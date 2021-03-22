from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home' ),
    path('products/',views.products1, name='products'),
    path('customers/',views.customers1, name='customers'),
    path('createorders1/',views.createorder, name='createorders1' ),
    path('updateorder/<str:pk_test>/',views.update_order, name='update_order' ),
    path('registration/',views.registerpage1, name='registration'),
    path('login/',views.loginpage, name='login'),
    path('logout/',views.logoutuser, name='logout'),
    path('createcustomer2/',views.createcustomer, name='createcustomer2')


]