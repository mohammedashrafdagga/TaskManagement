from django.urls import path
from .views import (
    UserCreationAPIView, UserLoginAPIView, UserLogoutAPIView
)

# app is account
app_name = 'api-auth'

urlpatterns = [
    path('register/', UserCreationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout')
]
