from django.urls import path
from .views import *

urlpatterns = [
    path('', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('decrement/<int:product_id>/', decrement, name='decrement'),
    path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'),
]
