from django.shortcuts import render,redirect
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
import random
from django.http import JsonResponse
from .helpers import send_forgot_email
import uuid
import pyotp



from .models import User

# Create your views here.

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        
        user=User.objects.filter(email=email).first()
        print(user)
        if user is None:
            raise AuthenticationFailed('user not found')
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        
        payload = {
            'id':user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat':datetime.datetime.utcnow()
            }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt':token
        }
        return response
    
    
class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        print(token)
        
        if not token:
            raise AuthenticationFailed("Incorrect password")
        
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Incorrect password")
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
class RandomView(APIView):
    def get(self,request):
    # Generate a random 4-digit OTP
        otp = ''.join(random.choice('0123456789') for _ in range(4))

    # You can save this OTP to the user's profile or session for later use
    # For example, request.session['otp'] = otp

    # In this example, we'll just return the OTP as a JSON response
        return JsonResponse({'otp': otp})
    
 
class ForgotPass(APIView):
    def post(self,request):
        try:
            email=request.data['email']
                    
            if not User.objects.filter(email=email).first():
                return JsonResponse({"message":"user not found"})
                    
            user_obj= User.objects.get(email=email)
            print(user_obj)
            token=str(uuid.uuid4())
            send_forgot_email(user_obj,token)
            return JsonResponse({"message":"email is sent"})
                
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Incorrect password")
        
        
class Otp_sent(APIView):
    def get(self,request):
        try:
        
            # Generate a random OTP
            totp = pyotp.TOTP(pyotp.random_base32(), interval=300)
            otp = totp.now()

                # Store OTP in the session
            request.session['otp'] = otp
            print(otp)

                # Send the OTP to the user (e.g., via SMS or email)

            return JsonResponse({'message': 'OTP sent successfully'})
        except Exception as e:
            print(e)
            
            
class Otp_varify(APIView):
    def post(self,request):
        try:
            user_otp = request.data['ottp']
            stored_otp = request.session.get('otp')

            if user_otp == stored_otp:
                    # OTP is correct, perform further authentication or redirect as needed
                return JsonResponse({"message":'authenticated_page'})
            else:
                return JsonResponse({'message': 'Invalid OTP'}, status=400)
        except Exception as e:
            print(e)

    
