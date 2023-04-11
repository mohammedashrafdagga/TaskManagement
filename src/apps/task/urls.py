from django.urls import path
from .views import (
    CreateTaskAPIView,
    TaskAssignAPIView,
    RemoveAssignToUserView,
)
app_name = 'api-task'


urlpatterns = [
    path('create/', CreateTaskAPIView.as_view(), name='create-task'),
    path('<slug:slug>/assign/',
         TaskAssignAPIView.as_view(), name='assign-task'),
    path('<slug:slug>/remove-assign/',
         RemoveAssignToUserView.as_view(), name='remove-assign')
]
