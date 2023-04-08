from rest_framework import serializers
from .models import Team


class TeamSerializer(serializers.ModelSerializer):
    leader = serializers.CharField(read_only=True)

    class Meta:
        model = Team
        fields = [
            'leader',
            'title',
            'bio',
            'create_at'
        ]

    def validate_leader(self, leader):
        team = Team.objects.filter(leader=leader).exists()
        if team:
            raise serializers.ValidationError(
                {'message': 'Already Have a Team, Cannot Create More Than One Team'})
        return leader
