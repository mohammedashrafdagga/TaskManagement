from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


def get_user_token(request):
    token_key = request.headers.get('Authorization').split(' ')[1]
    return get_object_or_404(Token, key=token_key).user
