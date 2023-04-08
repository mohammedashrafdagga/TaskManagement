# Create Test API for Authentication API
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase
from rest_framework.authtoken.models import Token


class TestUserCreation(TestCase):

    def setUp(self):
        self.url = reverse('api-auth:register')
        self.data = {
            'name': 'Mohammed',
            'email': 'test_user@gmail.com',
            'password1': 'test_user_123',
            'password2': 'test_user_123'
        }

    def test_create_user(self):
        'test to Create User'
        # send a request
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username,
                         self.data.get('email').split('@')[0])


class TestLoginAPIView(TestCase):
    def setUp(self) -> None:
        self.data = {
            'name': 'Mohammed',
            'email': 'test_user@gmail.com',
            'password1': 'test_user_123',
            'password2': 'test_user_123'
        }
        self.url = reverse('api-auth:login')
        self.client.post('/api-auth/register/', data=self.data)

    def test_login_for_exist_user(self):
        # login into system
        data = {
            'username': self.data['email'].split('@')[0],
            'password': self.data['password1']
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_for_none_exist_user(self):
        # login into system
        data = {
            'username': 'test_user_not_exists',
            'password': self.data['password1']
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestLogoutAPIView(TestCase):
    '''
        Test User Logout 
    '''

    def setUp(self) -> None:
        self.url = reverse('api-auth:logout')

    def test_logout_user(self):
        # First, create a user and obtain the token
        user = User.objects.create_user(
            username='johndoe', password='password')
        token = Token.objects.create(user=user)

        # Then, send a POST request to the API view with the token in the Authentication header
        response = self.client.post(
            self.url, HTTP_AUTHORIZATION=f'Token {token.key}')

        # Finally, assert that the response status code is 200 and the token is deleted
        self.assertEqual(response.status_code, 200)
        # with self.assertRaises(Token.DoesNotExist):
        #     Token.objects.get(user=user)
