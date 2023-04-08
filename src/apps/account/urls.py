from django.urls import path
from .views import (
    UserCreationAPIView, UserLoginAPIView, UserLogoutAPIView
)

# app is account
app_name = 'api-auth'

urlpatterns = [
    path('register/', UserCreationAPIView.as_views(), name='register'),
    path('login/', UserLoginAPIView.as_views(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout')
]
