from django.contrib import admin
from django.urls import path,include
from .views import RegisterView,LoginView,UserView,RandomView,ForgotPass,Otp_sent,Otp_varify,whatsapp,sms,ChallengesCreateAPIView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('user/', UserView.as_view()),
    path('sendotp/',RandomView.as_view()),
    path('forgotpass/',ForgotPass.as_view()),
    path('sentotp/',Otp_sent.as_view()),
    path('verify/',Otp_varify.as_view()),
    path('whatsappotp/',whatsapp.as_view()),
    path('sms/',sms.as_view()),
    path('challenges/', ChallengesCreateAPIView.as_view(), name='create_challenge_api'),
]






