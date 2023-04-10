from rest_framework import permissions, authentication, generics, status
from .serializers import TeamSerializer, TaskSerializer
from .models import Team, Task
from rest_framework.response import Response
from rest_framework.views import APIView
from .utils import get_user
from django.contrib.auth.models import User


class TeamCreateAPIView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # pop leader from data return
        data = serializer.data
        data.pop('leader')
        return Response({'status': 'success', 'data': data}, status=status.HTTP_201_CREATED)


class JoinTeamByCodeAPIView(APIView):
    'Using To Join A member for Team'

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        # get a user try to join
        user = get_user(request)

        # get team from code
        code = request.data.get('code')
        try:
            team = Team.objects.get(code=code)
        except Team.DoesNotExist:
            return Response(
                {'message': 'Invalid code'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # if team is leader for team
        if user == team.leader:
            return Response(
                {'message': 'you are leader for the team'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # if already join for team
        if team.member.filter(id=user.id).exists():
            return Response(
                {'message': 'you are already join them'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # otherwise
        team.member.add(user)
        return Response(
            {'message': 'You have successfully joined the team'},
            status=status.HTTP_200_OK
        )


class DeleteMemberAPIView(APIView):
    # To Getting User

    def post(self, request):
        user = get_user(request=request)

        # get team by using code of team
        code = request.data.get('code')
        try:
            team = Team.objects.get(code=code)
        except Team.DoesNotExist:
            return Response(
                {'message': 'Invalid code'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not team.member.filter(id=user.id).exists():
            return Response(
                {'message': 'The User not join to team to allow remove that'},
                status=status.HTTP_400_BAD_REQUEST
            )

        team.member.remove(user)
        return Response(
            {'message': 'You have successfully remove from this team the team'},
            status=status.HTTP_200_OK
        )


class CreateTaskAPIView(generics.CreateAPIView):
    ' Allow To Leader of Team Create Task and assign That'
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, *args, **kwargs):
        user = get_user(request)
        team_slug = request.data.get('team_slug')
        try:
            team = Team.objects.get(slug=team_slug)
        except Team.DoesNotExist:
            return Response(
                {'message': 'Invalid code'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if user != team.leader:
            return Response(
                {'message': 'you not allowed to create Task in this team'},
                status=status.HTTP_400_BAD_REQUEST
            )
        # how get assign to
        serializer = self.serializer_class(
            data=request.data, context={'team': team})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskAssignAPIView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'slug'
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def update(self, request, *args, **kwargs):
        leader = get_user(request)
        task = self.get_object()
        if leader != task.team.leader:
            return Response(
                {'message': 'not allowed access this task to update'},
                status=status.HTTP_400_BAD_REQUEST
            )
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)

        # if we have someone assign to task
        if task.assigned_to and user != task.assigned_to:
            return Response(
                {'message': 'we have someone already assign to task'},
                status=status.HTTP_400_BAD_REQUEST
            )

        task.assigned_to = user
        task.save()
        return Response(
            {'message': 'You have successfully assign this task'},
            status=status.HTTP_200_OK
        )


class RemoveAssignToUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, slug, *args, **kwargs):
        leader = get_user(request)
        try:
            task = Task.objects.get(slug=slug)
        except Task.DoesNotExist:
            return Response(
                {
                    'message': 'Invalid Task'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if leader != task.team.leader:
            return Response(
                {'message': 'not allowed access this task to update'},
                status=status.HTTP_400_BAD_REQUEST
            )
        task.assigned_to = None
        task.save()
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
