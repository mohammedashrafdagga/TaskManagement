from django.db import models
from django.contrib.auth import get_user_model
from .utils import get_random_string
import uuid
# Create your models here.


User = get_user_model()


class TeamManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


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

    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    code = models.CharField(max_length=6, default=get_random_string(6))

    objects = TeamManger()

    class Meta:
        ordering = ('-create_at', )

    def __str__(self):
        return self.title
