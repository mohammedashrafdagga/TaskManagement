from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        write_only=True, required=True,  max_length=100)
    password1 = serializers.CharField(
        write_only=True, required=True,  max_length=100)
    password2 = serializers.CharField(
        write_only=True, required=True,  max_length=100)

    class Meta:
        model = User
        fields = ('email', 'name', 'password1', 'password2')

    def validate(self, data):
        '''
            to validate data and clean that
        '''
        # the name update
        name = data.pop('name')
        name_parts = self.split_name(name)
        data.update(name_parts)

        # check the password is match oe not
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError('Password do not match!')

        # if match pop password2
        data.pop('password2')

        return data

    def validate_email(self, email):
        ''' valid email not exists '''
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                f'email: {email} is already exists, Use another one')
        return email

    def split_name(self, full_name):
        # split the name into first name and last name
        name_parts = full_name.split(' ', 1)
        first_name = name_parts[0]
        last_name = name_parts[1] if len(name_parts) > 1 else ''
        return {'first_name': first_name, 'last_name': last_name}

    def create(self, validated_data):
        '''
            Validated Data
        '''
        email = validated_data.pop('email')
        validate_email = self.validate_email(email)
        username = validate_email.split('@')[0]
        password = validated_data.pop('password1')
        return User.objects.create_user(username, email=email, password=password, **validated_data)
