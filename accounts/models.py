from django.db import models
from email.policy import default
from enum import unique
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AbstractUser

# Create your models here.
class UserAccountManager(BaseUserManager): #function to create user
    def create_user(self, first_name, last_name, username, email,  password = None):
        if not username:
            raise ValueError("User must have a username")
        
        if not email:
            raise ValueError("User must have an email")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    #create super user
    def create_superuser(self, first_name, last_name, username, email, password): # function to create and save super user
        user = self.create_user(
            email=email,
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password  
            
        )
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using = self._db)

        return user

# user creation fields
class User(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length = 50, unique=True)
    email = models.EmailField(max_length = 50, unique = True)
    phone_number = PhoneNumberField(max_length= 30, unique=True, null=True)

    date_joined = models.DateTimeField(auto_now_add = True)
    last_login = models.DateTimeField(auto_now = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default = True)
    is_superadmin = models.BooleanField(default = False)


    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email
    
    #to set permission for user
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
