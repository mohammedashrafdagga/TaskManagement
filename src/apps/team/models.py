from django.db import models
from django.contrib.auth.models import User
from .utils import generate_code
import uuid


class Team(models.Model):
    leader = models.OneToOneField(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='static/images/team_images/',
        default='static/images/team_images/team.jgp',
        blank=True, null=True
    )
    ''' date of created and updated '''
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # is active used in future
    is_active = models.BooleanField(default=True)
    # code for User
    code = models.CharField(max_length=6, default=generate_code)
    # member to join in team
    member = models.ManyToManyField(User, related_name='members')

    class Meta:
        ordering = ('-create_at', )

    def __str__(self):
        return self.title


# Task model
class Task(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('postponed', 'Postponed')
    ]

    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='in_progress')

    def __str__(self):
        return self.title
