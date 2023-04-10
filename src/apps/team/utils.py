import random
import string
from rest_framework.authtoken.models import Token

# Generate Random Number Using A Code to Join a Task


def generate_code():
    return ''.join(random.choices(string.digits, k=6))


def get_user(request):
    ' using to return User From Token'
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    return Token.objects.get(key=token).user
