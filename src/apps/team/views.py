from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main_page(request):
    '''
        Main Page for team
    '''
    return render(request, 'team/team_page.html')


@login_required
def create_team(request):
    '''
        Page for user allow to create team 
    '''
    return render(request, 'team/create_team.html')
