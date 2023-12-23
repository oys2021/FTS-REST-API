from django.db import models
from accounts.models import newUser
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_picture=models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=5, blank=True, null=True)
    phone=models.CharField(max_length=5, blank=True, null=True)
    
    def __str__(self):
        return str(self.user)
    
class Category(models.Model):
    name = models.CharField(max_length=25,blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Expense(models.Model):
    user_profile=models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    description=models.CharField(max_length=225)
    date = models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.amount
    
class Income(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.amount
    
    