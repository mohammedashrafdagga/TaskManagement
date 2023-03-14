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
