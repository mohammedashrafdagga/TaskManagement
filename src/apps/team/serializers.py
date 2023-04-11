from rest_framework import serializers
from .models import Team
from rest_framework.authtoken.models import Token



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['leader', 'title', 'bio']

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

