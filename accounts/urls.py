from django.urls import path
from django.views.decorators.csrf import csrf_exempt
# from .views import UserProfileViewSet
from .views import *
from .views import get_csrf_token
app_name = 'accounts'

urlpatterns = [
    # path('userprofiles/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='userprofile-list-create'),
    # path('userprofiles/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='userprofile-detail'),
    # # Add other URL patterns as needed
    path('signup', CreateUserView.as_view(), name="register"),
    path('login', UserLoginAPIView.as_view(), name="login"),
    path('verify', VerifyUser.as_view(), name="verify"),
    path('otp', OTPAPIView.as_view(), name="otp"),
    path('get_csrf_token/', get_csrf_token, name='get_csrf_token'),
]
