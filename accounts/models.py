from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,Group,Permission
from django.contrib.auth.base_user import BaseUserManager
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _ 




class FinanceManager(BaseUserManager):            
    
    def create_user(self,email,phone,password,**extra_fields):
        
        if not email:
            raise ValueError(_('You have to provide email address'))
        email=self.normalize_email(email)
        user=self.model(email=email,phone=phone,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, phone, password, **extra_fields):
        # Fix the typo here: change extra_fieldys to extra_fields
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        # Make sure to pass the 'username' parameter
        return self.create_user(email, phone, password, **extra_fields)
        
        


    
class newUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, unique=True)
    last_name= models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email'] # Change 'username' to 'user_name'
    objects = FinanceManager()
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.email or self.phone

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True