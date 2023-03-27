from django.urls import path
from . import views

# app is account
app_name = 'account'

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('register/', views.RegisterCreateAPIView.as_view(), name='register'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout')
]
