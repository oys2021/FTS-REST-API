from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from ftsApi.serializers import CategorySerializer, ExpenseSerializer, IncomeSerializer
from rest_framework.permissions import AllowAny
from ftsApi.models import Income, Expense, Category

# Create your views here.
class CategoryAPIView(CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class ExpenseAPIView(CreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [AllowAny]

class IncomeAPIView(CreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [AllowAny]

class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class IncomeList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class ExpenseList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
