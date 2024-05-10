from django.urls import path
from . import views

urlpatterns = [
    path('', views.merch, name='merch'),
    path('products/', views.products, name="products"),
    path('cart/', views.cart, name="cart"),
    path('products/<int:p_id>/', views.product_by_id, name="product"),
    path('cart/payment/', views.cart_payment, name="cart_payment"),
    path('cart/payment/cart_confirm/', views.cart_confirm, name="cart_confirm"),
    
]