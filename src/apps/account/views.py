from rest_framework import generics, status, permissions, authentication
from rest_framework.response import Response
from .serializers import UserCreationSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserCreationAPIView(generics.CreateAPIView):
    '''
        Using To allow for any User to Create Account into system
    '''
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserCreationSerializer

    def post(self, request, *args, **kwargs):
        # what we doing in post method
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        print(user)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            # update response data
            response_data = serializer.data
            response_data['username'] = user.username
            response_data['token'] = token.key
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response({"detail": "Authentication credentials were not provided."},
                        status=status.HTTP_401_UNAUTHORIZED)


class UserLoginAPIView(generics.GenericAPIView):
    '''
        login User to allow To antone to login into system
    '''
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user:
            # else return data
            user_token = Token.objects.get(user=user)
            response_data = {
                'username': username,
                'token': user_token.key
            }
            return Response({'data': response_data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


# Logout
class UserLogoutAPIView(generics.GenericAPIView):
    '''
        Delete User Account into System Using Token Access From User
    '''
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[0]

        # delete user token
        Token.objects.get(key=token).delete()

        return Response(status=status.HTTP_200_OK)
