from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


def get_user_token(request):
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[0]
    return get_object_or_404(Token, key=token).user
