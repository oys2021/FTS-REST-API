from django.urls import path
# from .views import UserProfileViewSet
from .views import *
app_name = 'accounts'

urlpatterns = [
    # path('userprofiles/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list-create'),
    # path('userprofiles/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='userprofile-detail'),
    # # Add other URL patterns as needed
    path('signup', CreateUserView.as_view(), name="register"),
    path('login', UserLoginAPIView.as_view(), name="login"),
    path('verify', VerifyUser.as_view(), name="verify"),
    path('otp', OTPAPIView.as_view(), name="otp"),
]
