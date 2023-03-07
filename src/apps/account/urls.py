from django.urls import path
from .views import register_page, activate_user, change_password, update_information
from django.contrib.auth import views as auth_views
from .forms import LoginForm

# app is account
app_name = 'account'

urlpatterns = [
    path('register/', register_page, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/',
         activate_user, name='activate'),
    # auth views
    path('login/',  auth_views.LoginView.as_view(
        template_name='account/login.html',
        form_class=LoginForm
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/auth/login/'), name='logout'),
    path('change-password/', change_password, name='change-password'),
    path('update-information/', update_information, name='update-information'),
]
