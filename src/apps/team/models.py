from django.db import models
from apps.account.models import Account
import uuid
# Create your models here.


# class Team(models.Model):
#     leader = models.OneToOneField(
#         Account, on_delete=models.SET_NULL, null=True)
#     title = models.CharField(max_length=250)
#     slug = models.SlugField(unique=True, default=uuid.uuid4)
#     bio = models.TextField(blank=True)
#     images = models.ImageField(
#         upload_to='team_images/', default='team_images/team.jgp')
#     members = models.ManyToManyField(Account, blank=True)
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     # if user delete Team
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         ordering = ('-create_at')

#     def __str__(self):
#         return self.title
