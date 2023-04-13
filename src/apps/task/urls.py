from django.urls import path
from .views import (
    CreateTaskAPIView,
    TaskAssignAPIView,
    RemoveAssignToUserView,
    UpdateTaskStatusAPIView,
    TaskSearchListAPIView
)
app_name = 'api-task'


urlpatterns = [
    path('create/', CreateTaskAPIView.as_view(), name='create-task'),
    path('<slug:slug>/assign/',
         TaskAssignAPIView.as_view(), name='assign-task'),
    path('<slug:slug>/remove-assign/',
         RemoveAssignToUserView.as_view(), name='remove-assign'),
    path('<slug:slug>/update-status/',
         UpdateTaskStatusAPIView.as_view(), name='task-update-status'),
    path('search/', TaskSearchListAPIView.as_view())
]
