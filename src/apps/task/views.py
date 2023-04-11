from django.shortcuts import render
from rest_framework import generics, views, permissions, authentication, status
from rest_framework.response import Response
from .serializers import TaskSerializer
from apps.team.models import Team
from rest_framework.authtoken.models import Token
from .models import Task
from django.contrib.auth.models import User
# Create your views here.


def get_user(request):
    ' using to return User From Token'
    token = request.META.get('HTTP_AUTHORIZATION').split(' ')[1]
    return Token.objects.get(key=token).user


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

        # if user already assign to task
        if user == task.assigned_to:
            return Response(
                {'message': 'you are already assign for this task'},
                status=status.HTTP_400_BAD_REQUEST
            )

        task.assigned_to = user
        task.save()
        return Response(
            {'message': 'You have successfully assign this task'},
            status=status.HTTP_200_OK
        )


class RemoveAssignToUserView(views.APIView):
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
