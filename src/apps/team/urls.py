from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('create/', views.TeamCreateAPIView.as_view(), name='create-team'),
    path('<slug:slug>/', views.TeamRetrieveAPIView.as_view(), name='team-detail')
]
