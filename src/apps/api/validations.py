from rest_framework import serializers
from apps.team.models import Team


def validate_leader(leader):
    team = Team.objects.filter(leader=leader).exists()
    if team:
        raise serializers.ValidationError(
            {'error': "you have a team, so can't create another one"})
    return leader
