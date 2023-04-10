from rest_framework import serializers
from .models import Team, Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.utils.text import slugify


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['leader', 'title', 'bio', 'due_date']

    def validate_leader(self, leader):
        if Team.objects.filter(leader=leader).exists():
            raise serializers.ValidationError(
                {'message': "Already Have A Team, you not allowed to create another one"}
            )
        return leader

    def get_token(self, request):
        '''
            get user from token in META Data
        '''
        token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
        return Token.objects.get(key=token).user

    def create(self, validated_data):
        leader = self.get_token(self.context['request'])
        leader = self.validate_leader(leader)
        validated_data['leader'] = leader

        return Team.objects.create(**validated_data)


class TaskSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date',
                  'assigned_to', 'slug', 'status']

    def validate_slug(self, slug):
        if Task.objects.filter(slug=slug).exists():
            raise serializers.ValidationError(
                {'message': 'The Task you Are create Already exists'}
            )
        return slug

    def create(self, validated_data):
        validated_data['team'] = self.context['team']
        slug = slugify(validated_data.get('title'))
        validated_data['slug'] = self.validate_slug(slug)
        return super().create(validated_data)
