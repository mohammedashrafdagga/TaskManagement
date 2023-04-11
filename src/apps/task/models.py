from django.db import models
from apps.team.models import Team
from django.contrib.auth.models import User
# Create your models here.

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
