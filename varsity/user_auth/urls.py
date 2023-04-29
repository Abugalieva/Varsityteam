from django.urls import path, include
from user_auth.views import RegisterUserAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, ResetPasswordAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('register/', RegisterUserAPIView.as_view(), name='registration'),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('change-password/', ChangePasswordAPIView.as_view()),
    path('forgot-password/', ForgotPasswordAPIView.as_view()),
    path('reset-password/<slug:token>/', ResetPasswordAPIView.as_view())
]