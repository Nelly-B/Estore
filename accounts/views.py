from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User

# Create your views here.

def  register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone_number = form.cleaned_data['phone_number']

            username = email.split('@')[0] #obtain username from email

            user = User.objects.create_user(first_name = first_name, last_name = last_name, email = email, password = password, username = username)

            user.phone_number = phone_number
            user.save()
    else:
        form = RegistrationForm()
            
    context ={
        'form' : form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect('/')
