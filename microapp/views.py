from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'menu_pages/home.html')

def products(request):
    return render(request, 'menu_pages/products.html')

def product_details(request):
    return render(request, 'menu_pages/product_details.html')

def cart(request):
    return render(request, 'menu_pages/cart.html')

def checkout(request):
    return render(request, 'menu_pages/checkout.html')

def account(request):
    return render(request, 'menu_pages/my-account.html')

def wishlist(request):
    return render(request, 'menu_pages/wishlist.html')

# def  login_register(request):
#     return render(request, 'menu_pages/register.html')

def  contact(request):
    return render(request, 'menu_pages/contact.html')


