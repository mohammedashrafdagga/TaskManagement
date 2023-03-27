from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class LoginAPIView(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            print(token)
            return Response(
                {'token': token.key},
                status=status.HTTP_200_OK
            )
        else:
            return Response({'error': 'Invalid Username or password'},
                            status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):

    def post(self, request, format=None):
        token_key = request.headers.get('Authorization').split(' ')[1]
        Token.objects.get(key=token_key).delete()
        return Response(status=status.HTTP_200_OK)


class RegisterCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def perform_create(self, serializer):
        return super().perform_create(serializer)
