from django.urls import path
from .views import main_page, create_team

app_name = 'team'

urlpatterns = [
    path('', main_page, name='team-main'),
    # path('<slug:slug>/detail/', team_detail, name='team-detail'),
    # path('join/<slug:slug>/<str:code>/', join_member, name='join_member'),
    path('create/', create_team, name='create-team'),
    # path('dashboard/', team_dashboard, name='dashboard'),

    # other operation for frontend
    # path('<slug:slug>/delete-member/<str:username>/', delete_member, name='delete-member'),
]
