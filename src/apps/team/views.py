from rest_framework import generics, status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import TeamSerializer
from .models import Team
from apps.api.utils import get_user_token
from apps.api.permissions import IsOwner
from apps.api.validations import validate_leader


class TeamCreateAPIView(generics.CreateAPIView):
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        user = get_user_token(self.request)
        leader = validate_leader(leader=user)
        serializer.save(leader=leader)
        return Response(status=status.HTTP_201_CREATED)


class TeamRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = 'slug'

    permission_classes = [
        IsOwner
    ]
