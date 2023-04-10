from django.urls import path
from .views import (
    TeamCreateAPIView, JoinTeamByCodeAPIView, DeleteMemberAPIView,
    CreateTaskAPIView)


app_name = 'api-team'

urlpatterns = [
    path('create/', TeamCreateAPIView.as_view(), name='create-team'),
    path('join-team/', JoinTeamByCodeAPIView.as_view(), name='join-team'),
    path('delete-member/', DeleteMemberAPIView.as_view(), name='delete-member'),
    path('tasks/create/', CreateTaskAPIView.as_view(), name='create-task')
]
