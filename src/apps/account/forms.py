from django import forms
from .models import Account
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

# login form to allow user login into system

User = get_user_model()


class LoginForm(AuthenticationForm):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


# register form that allow to user create a account

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        user = Account.objects.filter(email=email).exists()
        if user:
            raise forms.ValidationError('email Already Exists, Use another')
        # this is if not exists
        return email


class UserUpdateInformationForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ('email', 'username', 'name', 'bio', 'image')

    def clean_username(self):
        username = self.cleaned_data['username']
        user = Account.objects.filter(
            username=username).first()
        if user and user != self.instance:
            raise forms.ValidationError('The Username Already exists!')
        return username

