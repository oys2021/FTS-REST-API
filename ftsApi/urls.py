from django.urls import path
# from .views import UserProfileViewSet
from .views import CategoryList,IncomeAPIView,ExpenseAPIView,ExpenseList,IncomeList,CategoryAPIView
app_name = 'ftsApi'

urlpatterns = [
    # path('userprofiles/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list-create'),
    # path('userprofiles/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='userprofile-detail'),
    # # Add other URL patterns as needed
    path('categorylist',CategoryList.as_view(),name='categorylist'),
    path('expense',ExpenseAPIView.as_view(),name='expense'),
    path('income',IncomeAPIView.as_view(),name='income'),
    path('incomelist',IncomeList.as_view(),name='incomelist'),
    path('expenselist',ExpenseList.as_view(),name='expenselist'),
    path('category',CategoryAPIView.as_view(),name='categoryview'),
]
