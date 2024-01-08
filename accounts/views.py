from django.shortcuts import render
from django.core.mail import send_mail
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ftsApi.serializers import UserProfileSerializer,UserSerializer
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from ftsApi.models import UserProfile
from django.contrib.auth import authenticate,login
import random
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# from braces.views import CsrfExemptMixin

# Create your views here.

def sendEmail(subject, message, from_email, recipient):
    try:
        send_mail(subject, message, from_email, recipient)
        return True
    except Exception as e:
        print(e)
        return False

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class CreateUserView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer  # Assuming you have defined UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        username = serializer.validated_data['username']

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)

        elif User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            self.perform_create(serializer)

            # Log in the user
            user = authenticate(request, username=username, password=request.data['password'])
            if user:
                login(request, user)
                

                # Generate token
                token, created = Token.objects.get_or_create(user=user)

                # Generate OTP
                otp = ''.join(str(random.randint(0, 9)) for i in range(5))

                # Update UserProfile with OTP
                UserProfile.objects.create(user=user, otp=otp)

                # Send OTP to user
                send_mail('OTP', 'Your OTP is ' + otp, 'IncomeChecker.com', [email], fail_silently=True)
                
                if user.is_authenticated:
                    token_data = {"token": token.key}
                    return Response({'token': token.key, 'message': 'User created and logged in'}, status=status.HTTP_201_CREATED)
                    
                else:
                    return Response({'error': 'Authentication failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            else:
                return Response({'error': 'Authentication failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                               
class VerifyUser(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = dict(request.data)
        user = request.user if request.user.is_authenticated else None

        if user:
            regular_user = UserProfile.objects.get(user=user)
        
            if regular_user.otp == data['otp']:
                regular_user.verified = True
                regular_user.save()
                
                # Assuming you want to generate a new token after verification
                token, created = Token.objects.get_or_create(user=user)

                return Response({'token': token.key, 'message': 'Verification successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid OTP.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'User not authenticated.'}, status=status.HTTP_401_UNAUTHORIZED)            


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        data = dict(request.data)
        user = authenticate(username=data['username'], password=data['password'])

        if user is not None and user.userprofile.verified:
            # User is verified, proceed to generate or retrieve the token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'message': 'Login successful.'}, status=status.HTTP_200_OK)
        elif user is None:
            return Response({'error': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
        elif not user.userprofile.verified:
            return Response({'error': 'User not verified.'}, status=status.HTTP_400_BAD_REQUEST)

            
class OTPAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
            data = dict(request.data)
            try:
                user = User.objects.get(email=data['email'])
                user = UserProfile.objects.get(user=user)
                otp = ''.join(str(random.randint(0,9)) for i in range(4))
                user.otp = otp
                user.save()
                send_mail('OTP', 'Your OTP is ' + otp, 'dryce.com', [data['email']], fail_silently=True)
                return Response({"message": "OTP sent."},status=status.HTTP_200_OK)
            except:
                return Response({"error":"Your email does not exist"},status=status.HTTP_400_BAD_REQUEST)
    
class ResetPasswordView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self,request):
        data=dict(request.data)
        user = User.objects.get(email=data['email'])
        regular_user = UserProfile.objects.get(user=user)
        
        # OI THIS IS WRONG
        if data['otp'] == regular_user.otp:
            user.set_password(data['password'])
            user.save()
            return Response(status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "data is incorrect"},status=status.HTTP_400_BAD_REQUEST)
        
from django.http import JsonResponse

def get_csrf_token(request):
    return JsonResponse({'csrf_token': request.csrf_token})