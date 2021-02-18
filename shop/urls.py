from django.urls import path , include
from . import views

app_name='shop'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),
    path('checkout/',views.checkout,name='checkout'),
    path('cart/',views.userCart,name='cart'),
]