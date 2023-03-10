from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Team


@login_required
def main_page(request):
    '''
        Main Page for team
    '''
    # print(request.user)
    my_teams = Team.objects.filter(leader=request.user)
    # leader have just one team -> the related_name not use here
    joined_teams = request.user.members.all()
    return render(request, 'team/team_page.html', {'my_teams': my_teams, 'joined_teams': joined_teams})


@login_required
def create_team(request):
    '''
        Page for user allow to create team 
    '''
    return render(request, 'team/create_team.html')
