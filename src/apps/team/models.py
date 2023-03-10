from django.db import models
from apps.account.models import Account
from .utils import get_random_string
import uuid
# Create your models here.


class TeamManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class Team(models.Model):
    leader = models.OneToOneField(
        Account, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, default=uuid.uuid4)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='team_images/', default='team_images/team.jgp')
    members = models.ManyToManyField(
        Account, blank=True, related_name='members')
    # Account.members_set.all() -> return all team i joined it
    # (but relation i clear is one user to one team join for now)
    # as know one team can contains many members
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # if user delete Team- convert is_active to false
    # keep save for statically
    is_active = models.BooleanField(default=True)

    # code to share with user to join this team
    code = models.CharField(max_length=6, default=get_random_string(6))
    # Set Customize Objects
    objects = TeamManger()

    class Meta:
        ordering = ('-create_at', )

    def __str__(self):
        return self.title
