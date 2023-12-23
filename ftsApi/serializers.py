from rest_framework import serializers
from .models import UserProfile,Expense,Income,Category
from django.contrib.auth import get_user_model
User = get_user_model() 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=('username','email','password','is_active', 'date_joined', 'last_login')
        write_only_fields = ('password')
        read_only_fields = ('is_staff', 'is_superuser', 'is_active', 'date_joined', 'last_login')
        
    def create(self, validated_data):
            password= validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            
            instance.is_active = True
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields =fields = ('id','user', 'verified','profile_picture','name','address', 'phone')
        
class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'otp', 'password',)
        
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields = '__all__'
        
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Income
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'