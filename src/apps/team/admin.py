from django.contrib import admin
from .models import Team, Task
# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['leader', 'title', 'code', 'create_at']

    def get_readonly_fields(self, request, obj):
        return [f.name for f in self.model._meta.fields]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['team', 'title', 'slug', 'due_date']

    def get_readonly_fields(self, request, obj):
        return [f.name for f in self.model._meta.fields]
