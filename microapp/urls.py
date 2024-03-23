from django.urls import path
from .views import index, products, product_details, cart, checkout, account, wishlist, login_register, contact

urlpatterns = [
    path('index/', index, name='index'),
    path('products/', products, name='products'),
    path('product_details/', product_details, name='details_product' ),
    path('cart/', cart, name='carts' ),
    path('checkout/', checkout, name='checkouts'),
    path('my_account/', account, name='my_account'),
    path('wishlist/', wishlist, name='wish'),
    path('login_register/', login_register, name='register'),
    path('contact/', contact,  name='contact'),
]