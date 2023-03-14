from rest_framework import serializers
from django.contrib.auth import get_user_model


# User model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]

    def validate_email(self, value):
        user = User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError(f'the {value} is already exists')
        else:
            return value
