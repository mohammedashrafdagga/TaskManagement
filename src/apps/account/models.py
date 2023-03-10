from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin, AbstractBaseUser
from django.core.mail import send_mail


class UserManger(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # super user
    def create_superuser(self, email,  password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email,  password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    # field
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_images/',
                              default='user_images/default.png')
    bio = models.TextField(blank=True)
    # for user
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # time and date
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # set objects
    objects = UserManger()

    def __str__(self) -> str:
        return self.username.capitalize()

    # send email
    # email user
    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )
